
"""
データベースの情報が入ったjsonファイルを作成する
import json

db_info_dict = {
    'sample_db': {
        'db_name': 'sample_db',
        'port': 3306,
        'user_name': 'root',
        'pass': 'root'
    }
}
with open('db_conf.json', 'w') as json_file:
    json.dump(db_info_dict, json_file,indent=True)
"""
import json


def load_db_json():
    """
    データベースの構成情報をjsonファイルから取得する
    """
    with open('db_conf.json', 'r') as dc_json_file:
        db_conf = json.load(dc_json_file)
    return db_conf


def main():
    db_conf = load_db_json()
    sample_db = db_conf['sample_db']
    print('##############################################')
    print('[DATABASE CONFIGURATION]')
    print('database_name : ' + sample_db['db_name'])
    print('port : ' + str(sample_db['port']))
    print('user_name : ' + sample_db['user_name'])
    print('password : ' + sample_db['pass'])
    print('##############################################')


if __name__ == '__main__':
    main()
