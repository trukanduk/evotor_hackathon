import science.suggester.suggester as suggester

import science.suggester.data_preprocessing as data_preprocessing

SHOPS_TO_DUMP = ["17846", "23293", "10171", "11013", "58864", "108664"]


def _main():
    data_sorted = data_preprocessing.get_data()
    print("Got sorted data")

    checks = data_preprocessing.get_checks(data_sorted)
    print("Got checks data")

    w2v_model = data_preprocessing.get_w2v_model(checks)
    print("Got w2v model")

    shops, features = data_preprocessing.calc_features(data_sorted, w2v_model)
    print("Got shops features to find similar")

    distance_dict = data_preprocessing.calculate_distance_between_shops(shops, features)
    print("Got distance (in terms of assortment) between shops")

    shop_to_goods, good_to_name = data_preprocessing.get_goods_data(data_sorted)
    print("Got goods data")

    suggester.dump_shops(SHOPS_TO_DUMP, distance_dict, shop_to_goods, good_to_name, filename="suggests_for_shops.csv")
    print("Dumped suggestions")


if __name__ == '__main__':
    _main()