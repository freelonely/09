from tools.Random import randomSample, randomSample2


def test ():
    print('start')
    file = open(r'E:\Project\IdeaJAVA\xd\GalaxywalletAutotest\testfile\MarkCenterInsert.sql','w')
    for x in range(0, 5):
        str = u"INSERT INTO `finance_data_aggregation`.`user` (`id`, `uid`, `name`, `mobile`, `gender`, `data_source`, `db_source`, `product_source`, `channel`, `device_type_user`, `ctime`, `app_ver`, `app_os`, `device_type`, `sdk_ver`, `login_ftime`, `login_ltime`, `race`, `id_no`, `address`, `expire_date`, `id_time`, `face_time`, `base_info_time`, `job_info_time`, `contact_time`, `history_time`, `old_user_flag`, `user_status`) VALUES ('%s', '%s', 'lijunfeng', '%s', '1', '3', '2', '3', 'himi_com', '1', '2019-04-09 18:00:41', '1.6.0', '1', 'PBAM00', '27', '2019-04-09 18:00:41', '2019-04-10 10:22:56', '汉', '110222198502052910', '北京市顺义区南法信地区十里堡村北小街7号', '2035-02-09 00:00:00', '2019-04-10 16:56:19', '2019-04-09 18:52:50', '2019-04-09 18:54:39', '2019-04-09 18:54:39', '2019-04-09 18:52:54', '2019-04-10 09:46:50', '0', '3');" %(randomSample(),randomSample(),'18032'+randomSample2())
        str.encode('UTF-8')
        file.write(str+'\n')
        # print(str)
    file.close()
    print('over')

test()