import editdistance


def normalize_name(name):
    return " ".join(filter(lambda x: len(x) > 6, name.decode("utf-8").lower().encode("utf-8").split()))


def is_legal_name(normalized_name, normalized_cur_names):
    FORBIDDEN_SUBSTR = ["акция", "свободной", "пэт", "обслуживание", "пакет"]
    splitted = set(normalized_name.split())
    for name_to_check in normalized_cur_names:
        if editdistance.eval(name_to_check, normalized_name) < 3:
            return False
        if len(splitted) > 3 and len(splitted.difference(name_to_check.split())) == 1:
            return False

    if any(map(lambda x: x in normalized_name.decode("utf-8").lower().encode("utf-8"), FORBIDDEN_SUBSTR)):
        return False

    return True


def suggester(shop, distance_dict, shop_to_goods, good_to_name):
    sim_shops = sorted(distance_dict[shop], key=lambda x: x[1][0])
    sim_shops = filter(lambda x: shop_to_goods[x[0]]["total"] > 700, sim_shops)
    cur_shop_good_names = map(lambda x: good_to_name[x], filter(lambda key: key != "total", shop_to_goods[shop].keys()))
    normalized_cur_names = map(normalize_name, cur_shop_good_names)
    candidates = {}
    for shop_candidate in sim_shops[:3]:
        for good in shop_to_goods[shop_candidate[0]]:
            if good == "total":
                continue
            name = normalize_name(good_to_name[good])
            if is_legal_name(name, normalized_cur_names):
                if name not in candidates:
                    candidates[name] = [shop_to_goods[shop_candidate[0]][good]["qnt"], good_to_name[good], good]
                else:
                    candidates[name][0] += shop_to_goods[shop_candidate[0]][good]["qnt"]
    return sorted(candidates.items(), key=lambda x: x[1], reverse=True)[:10]


def dump_shops(shops_to_dump, distance_dict, shop_to_goods, good_to_name, filename="suggests_for_shops.csv"):
    to_dump = []
    for shop in shops_to_dump:
        temp = map(lambda x: x[1][2], suggester(int(shop), distance_dict, shop_to_goods, good_to_name))
        while len(temp) < 10:
            temp += [0]
        to_dump += [np.array(temp)]
    df_to_dump = pd.DataFrame(np.column_stack(to_dump), columns=shops_to_dump)
    df_to_dump.to_csv(path_or_buf="./" + filename, index=False, header=True)