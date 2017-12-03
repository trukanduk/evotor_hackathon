import pandas as pd
import numpy as np
import scipy.spatial
import gensim
from joblib import Parallel, delayed


COLUMNS = ["id",
           "good_id",
           "set_id",
           "oper_date",
           "device_id",
           "shop_id",
           "check_type",
           "total_cost",
           "total_cashback",
           "total_discount",
           "total_tax_pc",
           "total_tax",
           "items_count",
           "item_name",
           "item_type",
           "um",
           "qnt",
           "price",
           "sum_price",
           "oper_discount",
           "oper_discount_pc",
           "result_sum",
           "purchase_price",
           "onhand_qnt",
           "region",
           "inn",
           "okved_full",
           "okved_description",
           "lat",
           "lng",
           "category_id",
           "category_name"]

names_to_index = dict(zip(COLUMNS, range(len(COLUMNS))))

CATEGS_COUNT = 55
W2V_LENGTH = 150


def get_data(filename="hakaton-fin.csv"):
    df = pd.read_csv(filename, names=COLUMNS)
    data_sorted = np.array(sorted(df.values,
                                  key=lambda x: (x[names_to_index["shop_id"]],
                                                 x[names_to_index["set_id"]],
                                                 x[names_to_index["good_id"]])
                                  ))

    return data_sorted


def get_checks(data_sorted):
    set_id_index = names_to_index["set_id"]
    good_id_index = names_to_index["good_id"]
    checks = []
    current_check = []
    prev_check_id = None
    for row in data_sorted:
        check_id = row[set_id_index]
        if check_id != prev_check_id:
            if prev_check_id is not None:
                temp = list(map(str, np.unique(current_check)))
                if len(temp) >= 3:
                    np.random.shuffle(temp)
                    checks += [temp]
            prev_check_id = check_id
            current_check = []
        current_check += [row[good_id_index]]

    return np.array(checks)


def get_w2v_model(checks, reload=False):
    if reload:
        return gensim.models.Word2Vec("basic_word2vec_model")
    else:
        model = gensim.models.word2vec.Word2Vec(checks, workers=12, size=150, min_count=10, window=10, sample=0.0001,
                                                seed=1234)
        model.init_sims(replace=True)
        model.save("basic_word2vec_model")

        return model


def calc_features(data_sorted, model):
    uniq_categs = np.unique(data_sorted[:, names_to_index["category_id"]], return_counts=True)
    categs_map = dict(list(zip(uniq_categs[0], list(range(len(uniq_categs[0]))))))

    prev_shop_id = None
    prev_check_id = None
    prev_good_id = None
    shops = []
    features = []
    shop_categories = np.zeros(shape=CATEGS_COUNT)
    checks_price = []
    items_total = 0
    income_total = 0
    w2v_vector = np.zeros(W2V_LENGTH)
    for row in data_sorted:
        shop_id = row[names_to_index["shop_id"]]
        check_id = row[names_to_index["set_id"]]
        good_id = row[names_to_index["good_id"]]

        if shop_id != prev_shop_id:
            if prev_shop_id is not None:
                shops += [prev_shop_id]

                if items_total > 1e-6:
                    mean_price = income_total / items_total
                else:
                    mean_price = 0.0

                if w2v_den > 0:
                    w2v_vector

                features += [np.concatenate((
                    [np.mean(checks_price), mean_price],
                    shop_categories,
                    w2v_vector))]

            checks_price = []
            items_total = 0
            income_total = 0
            prev_shop_id = shop_id
            w2v_vector = np.zeros(W2V_LENGTH)
            shop_categories = np.zeros(shape=CATEGS_COUNT)
            w2v_den = 0
        if check_id != prev_check_id:
            checks_price += [row[names_to_index["total_cost"]]]
            prev_check_id = check_id

        if good_id != prev_good_id:
            if str(good_id) in model:
                w2v_vector += model[str(good_id)]

        items_total += row[names_to_index["qnt"]]
        income_total += row[names_to_index["result_sum"]]
        shop_categories[categs_map[row[names_to_index["category_id"]]]] += 1

    if items_total > 1e-6:
        mean_price = income_total / items_total
    else:
        mean_price = 0.0

    shops += [prev_shop_id]
    features += [np.concatenate((
        [np.mean(checks_price), mean_price],
        1.0 * shop_categories / np.sum(shop_categories),
        w2v_vector))]

    shops = np.array(shops)
    features = np.array(features)

    return shops, features


def distance_function(vector1, vector2):
    if np.abs(np.sum(vector1[-CATEGS_COUNT - W2V_LENGTH:-W2V_LENGTH] * vector2[
                                                                       -CATEGS_COUNT - W2V_LENGTH:-W2V_LENGTH])) < 1e-6:
        categs_cosine = -1000
    else:
        categs_cosine = 1 - scipy.spatial.distance.cosine(vector1[-CATEGS_COUNT - W2V_LENGTH:-W2V_LENGTH],
                                                          vector2[-CATEGS_COUNT - W2V_LENGTH:-W2V_LENGTH])
    if np.abs(np.sum(vector1[-W2V_LENGTH:] * vector2[-W2V_LENGTH:])) < 1e-6:
        w2v_cosine = -1000
    else:
        w2v_cosine = 1 - scipy.spatial.distance.cosine(vector1[-W2V_LENGTH:], vector2[-W2V_LENGTH:])
    mean_checks_ratio = vector1[0] / (vector2[0] + 1e-6)
    mean_price_ratio = vector1[1] / (vector2[1] + 1e-6)

    if categs_cosine < 0 or w2v_cosine < 0 or categs_cosine * w2v_cosine < 0.8:
        return None

    if mean_checks_ratio < 0:
        mean_checks_ratio = 1000000
    if mean_price_ratio < 0:
        mean_price_ratio = 1000000

    return (1 - categs_cosine) * (1 - w2v_cosine) * max(mean_checks_ratio, 1 / (mean_checks_ratio + 1e-6)) * max(
        mean_price_ratio, 1 / (mean_price_ratio + 1e-6)), categs_cosine, w2v_cosine, mean_checks_ratio, mean_price_ratio


def calc_dist(shop1, shops, features, shop_to_features_id):
    temp = []
    i = shop_to_features_id[shop1]
    for shop2 in shops:
        if shop1 == shop2:
            continue
        j = shop_to_features_id[shop2]
        ret = distance_function(features[i], features[j])
        if ret is not None:
            temp += [(shop2, ret)]
    return shop1, temp


def calculate_distance_between_shops(shops, features):
    shop_to_features_id = dict(zip(shops, range(len(shops))))
    r = Parallel(n_jobs=10, verbose=5)(delayed(calc_dist)(shop1, shops, features, shop_to_features_id) for shop1 in shops)
    return dict(r)


def get_goods_data(data_sorted):
    shop_to_goods = {}
    good_to_name = {}
    prev_shop = None
    current_shop_data = {}
    for row in data_sorted:
        current_shop = row[names_to_index["shop_id"]]
        if current_shop != prev_shop:
            if prev_shop is not None:
                shop_to_goods[prev_shop] = current_shop_data

                current_shop_data["total"] = 0
                for good_id in current_shop_data:
                    if good_id == "total":
                        continue
                    if current_shop_data[good_id]["qnt"] > 0:
                        current_shop_data[good_id]["profit_per_qnt"] = current_shop_data[good_id]["total_profit"] / \
                                                                       current_shop_data[good_id]["qnt"]
                    else:
                        current_shop_data[good_id]["profit_per_qnt"] = 0.0
                    current_shop_data["total"] += current_shop_data[good_id]["qnt"]

            prev_shop = current_shop
            current_shop_data = {}

        good_id = row[names_to_index["good_id"]]
        if good_id not in good_to_name:
            good_to_name[good_id] = row[names_to_index["item_name"]]

        qnt = row[names_to_index["qnt"]]
        purchase_price = row[names_to_index["purchase_price"]]
        profit = row[names_to_index["result_sum"]] - qnt * purchase_price
        if good_id not in current_shop_data:
            current_shop_data[good_id] = {}
            current_shop_data[good_id]["total_profit"] = profit
            current_shop_data[good_id]["qnt"] = qnt
            current_shop_data[good_id]["purchase_price"] = purchase_price
        else:
            current_shop_data[good_id]["total_profit"] += profit
            current_shop_data[good_id]["qnt"] += qnt

    return shop_to_goods, good_to_name

