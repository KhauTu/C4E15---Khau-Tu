from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

customer = db['customers']
post = db['posts']

post_list = post.find()
# post_KT = post.remove({"title": "Ếch xanh"})

# for p in post_list:
#     print(p['author'])
    # if p["author"] == "Khau Tú":
    #     print(p['content'])
my_post = '''
(Our class is so fun, Best wishest for next C4E classes)

Trong một cái đầm nhỏ,
Trên một chiếc lá sen,
Chễm chệ một chú ếch,
Màu xanh, đốm mắt đen

Chú ngước mắt nhìn trời
Mắt không có màu xanh
Vì nay trời đi vắng
Bầu trời không trong lành
#1
Ngày xửa ngày xưa, trong một khu rừng nọ, có một chiếc đầm nhỏ.
Ngày ngày có một chú ếch vẫn thường ngồi trên lá sen. Gặp ai ghé ngang qua chú cũng hỏi "trời mưa có màu gì?" Bởi vì chú rất tò mò, mỗi khi trời không mưa, chú ngước đôi mắt trong veo lên nhìn, thì cả bầu trời và cả mặt hồ mênh mông đều cùng một vẻ.
Nhưng khi trời dổ mưa, đôi mắt nhìn trời của chú ướt nhòe đi vì nước trút, có cúi xuống nhìn mặt hồ thì cũng chỉ thấy những vòng tròn loang loáng...
Từng hạt mưa cứ tí tách, tí tách nhảy múa trước mặt chú, mỗi bọt nước bắn tung lên tựa hồ như chiếc vương miện thủy tinh trong suốt, mà chú thầm ao ước được đội lên đầu...

-Ừ thì trời mưa nhỉ?
Ếch ồm ộp tự hỏi:
- Trời mưa có màu gì?
Nước trút mãi không thôi

Mưa cứ trút, cứ trút
Lá cứ trôi, cứ trôi,
Lặng lẽ nhắm đôi mắt
Ếch ta thấm mệt rồi!
#2
Chú ếch này từ đâu đến, không ai biết cả. cũng không ai biết chú sẽ đi về đâu. Chỉ biết rằng ếch ta thật kỳ lạ, ngồi trên lá sen suốt cả ngày, hết ngắm trời rồi ngắm nước. Ruồi muỗi bay qua, chú cũng chẳng thèm ngó tới, nhện chăng tơ trước mặt chú cũng làm thinh; kể cả khi cái bụng ùng ục biểu tình, chú cũng chẳng buồn đưa lưỡi liếm mép. Vì chú thuộc trường phái ăn chay. À, mà cũng không hẳn, người ta ăn chay thì cũng ăn rau ăn cỏ, còn chú thì chỉ ăn sương, uống gió, hấp thụ ánh mặt trời.
Dưới cơn mưa cuối hạ, trong cơn mơ mộng mị, Ếch ta thấy mình hóa thân là một chàng hoàng tử, sống trong một lâu đài xa hoa. Nơi đó có vườn thượng uyển, có tòa lâu đài nguy nga, cổ kính. Nhưng chợt từ đâu, mây giông kéo về làm u ám cả giấc mơ. Một mụ phù thủy hiện ra, với cây đũa phép trên tay, mụ vung lên một cái, cả bầu trời rung chuyển. Và chàng hoàng tử bạch mã bị lời nguyền biến thành ếch.
Ếch ta chợt choàng tỉnh giấc sau tiếng sét nổ đùng đoàng. Chàng tự nhủ thầm, hóa ra mụ phù thủy chỉ là giấc mơ. Và chàng vẫn chỉ là ếch. Mưa vẫn tí tách…
'''
new_post = {
    "title": "Ếch xanh",
    "author": "Khau Tú",
    "content": my_post
}
post.insert_one(new_post)
