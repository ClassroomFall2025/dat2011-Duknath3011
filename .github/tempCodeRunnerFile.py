def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
    banh_dau_xanh = {"duong:":0.04, "dau:":0.07}
    banh_thap_cam = {"duong:":0.06, "dau:":0}
    banh_deo = {"duong:":0.05, "dau:":0.02}
    nguyen_lieu ={}
    duong_hop_banh = sl_bdx * banh_dau_xanh["duong:"] + sl_btc * banh_thap_cam["duong:"] + sl_bd * banh_deo["duong:"]
    dau_hop_banh = sl_bdx * banh_dau_xanh["dau:"] + sl_btc * banh_thap_cam["dau:"] + sl_bd * banh_deo["dau:"]
    nguyen_lieu = {"sugar": duong_hop_banh, "bean": dau_hop_banh}
    return nguyen_lieu
print(tinh_nguyen_lieu(1,2,3))