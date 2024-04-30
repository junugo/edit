import qrcode
from PIL import Image, ImageDraw, ImageFont
class answer_sheet_generator:
    def __init__(self):
        self.font_path="resource/文泉驿正黑体wqy-zenhei.ttc"
        self.font_size=25
        self.original_photo="resource/normal_card.png"
        self.QR_version=1
        self.top=300
        self.column1=25
        self.interval=100
        self.column2=575
        self.QR_Size=150
        self.QR_x=100
        self.QR_y=100
    def make(self,Race_Name:str,QR:str,text:str,List:list):
        original=Image.open(self.original_photo)
        draw = ImageDraw.Draw(original)
        def draw_text(text:str,x,y,Front_Size=self.font_size):
            Front=ImageFont.truetype(self.font_path, Front_Size)
            text_position = (x,y)
            draw.text(text_position, text, font=Front, fill="black")  # 填充颜色为黑色
        if len(List)<=7:
            for i in range(len(List)):
                draw_text(List[i]["Class"],self.column1,self.top+i*200)
                draw_text(List[i]["Name"],self.column1+self.interval,self.top+i*200)
        else:
            for i in range(7):
                draw_text(List[i]["Class"],self.column1,self.top+i*200)
                draw_text(List[i]["Name"],self.column1+self.interval,self.top+i*200)
            for i in range(7,len(List)):
                draw_text(List[i]["Class"],self.column2,self.top+(i-7)*200)
                draw_text(List[i]["Name"],self.column2+self.interval,self.top+(i-7)*200)

        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1,
        )
        qr.add_data(QR)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")
        img_qr = img_qr.resize((self.QR_Size, self.QR_Size))
        original.paste(img_qr, (self.QR_x,self.QR_y))
        draw_text(text,self.QR_x,self.QR_y+self.QR_Size)
        draw_text(Race_Name,300,100,100)
        original.save("Temp/a.png")

if __name__=="__main__":
    answer_sheet_generator=answer_sheet_generator()
    QR="114514"
    data=[{"Class":"912","Name":"JUNU"},{"Class":"912","Name":"JUNU"},{"Class":"912","Name":"JUNU"},{"Class":"912","Name":"JUNU"},{"Class":"912","Name":"JUNU"},{"Class":"912","Name":"JUNU"},{"Class":"912","Name":"JUNU"},{"Class":"912","Name":"JUNU"}]
    answer_sheet_generator.make("九年级男子实心球",QR+" 这是您的场次编号，如果您无法登录系统，请将答题卡送至登分处","No. "+QR,data)