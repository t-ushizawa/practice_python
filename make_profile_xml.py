"""
ユーザーが入力したprofileのxmlファイルを作成する
"""
import xml.etree.ElementTree as ET


def create_user_profile(name=None, age=None, height=None, hobby=None):
    """
    引数に合わせてXMLファイルを作成する
    """
    root = ET.Element('root')
    tree = ET.ElementTree(element=root)
    profile = ET.SubElement(root, 'Profile')
    user1 = ET.SubElement(profile, 'user1')
    e_name = ET.SubElement(user1, 'name')
    e_name.text = name
    e_age = ET.SubElement(user1, 'age')
    e_age.text = age
    e_height = ET.SubElement(user1, 'height')
    e_height.text = height
    e_hobby = ET.SubElement(user1, 'hobby')
    e_hobby.text = hobby
    tree.write('profile.xml', encoding='utf-8', xml_declaration=True)


def main():
    """
    ユーザーにプロフィールを入力させる
    """
    name = input('名前：')
    age = input('年齢：')
    height = input('身長：')
    hobby = input('趣味：')
    create_user_profile(name, age, height, hobby)


if __name__ == '__main__':
    main()


