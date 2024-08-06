import requests

from bs4 import BeautifulSoup

session = requests.Session()

# URL of the login action
url = 'https://lumanager.net/login/login'

# Form data to be submitted
payload = {
    'login': 'nhoxtin15',
    'register': '0',  # Assuming you already have an account
    'password': 'nhoxtin1',
    'remember': '1',  # Optional: If you want to maintain login session
    'cookie_check': '1',
    'redirect': '/',
    '_xfToken': ''  # You may need to obtain and fill this token if it's dynamic
}


cookie = session.get(url).cookies

# Sending POST request to login
response = session.post(url, data=payload,cookies=cookie)
cookie = response.cookies

result = open("result.html", "w")
# result.write(response.text)

print(cookie)

response = session.get('https://lumanager.net/forums/rao-vat-dich-vu-khac.40/create-thread')
# result.write(response.text)







url = 'https://lumanager.net/forums/rao-vat-dich-vu-khac.40/add-thread'
response = session.get(url,cookies=cookie)

beautify = BeautifulSoup(response.text, 'html.parser')
token = beautify.find('input', {'name': '_xfToken'}).get('value')
print(token)


# # Define the form data
form_data = {
    'title': 'Thiết kế website trọn gói giá rẻ',
    'message_html': '''[b]Giới thiệu [URL='https://canhcam.vn']Thiết kế Website[/URL] bởi Cánh Cam[/b]<br><br>
	Cánh Cam là một công ty chuyên cung cấp dịch vụ thiết kế website chuyên nghiệp, với đội ngũ nhân viên giàu kinh nghiệm, sáng tạo và đam mê. Chúng tôi luôn nỗ lực mang đến cho khách hàng những giải pháp tối ưu nhất, giúp họ xây dựng website hiệu quả, thu hút khách hàng và nâng cao thương hiệu.
	[b]abcdDịch vụ thiết kế website của Cánh Cam bao gồm:[/b]
	[b]Thiết kế website chuẩn SEO:[/b] Tối ưu hóa website theo tiêu chuẩn Google, giúp website dễ dàng được tìm kiếm và xếp hạng cao trên công cụ tìm kiếm.
	[b]Thiết kế website responsive:[/b] Website hiển thị đẹp và đầy đủ chức năng trên mọi thiết bị, từ máy tính để bàn đến điện thoại di động.
	[b]Thiết kế website theo yêu cầu:[/b] Cánh Cam thiết kế website đáp ứng mọi yêu cầu của khách hàng, từ giao diện, chức năng cho đến nội dung.
	[b]Quản trị website dễ dàng:[/b] Cánh Cam cung cấp hệ thống quản trị website đơn giản, giúp khách hàng dễ dàng cập nhật nội dung, hình ảnh và quản lý website của mình.
	[b]Hỗ trợ kỹ thuật chuyên nghiệp:[/b] Cánh Cam cung cấp dịch vụ hỗ trợ kỹ thuật 24/7, giải quyết mọi vấn đề phát sinh cho khách hàng.
	[b]Lợi ích khi sử dụng dịch vụ thiết kế website của Cánh Cam:[/b]
	[b]Website chuyên nghiệp, đẹp mắt và hiệu quả:[/b] Tăng cường hình ảnh thương hiệu, thu hút khách hàng và nâng cao doanh thu.
	[b]Tối ưu hóa website cho công cụ tìm kiếm:[/b] Giúp website dễ dàng được tìm kiếm và xếp hạng cao trên Google, thu hút nhiều khách hàng tiềm năng.
	[b]Tiết kiệm thời gian và chi phí:[/b] Cánh Cam sẽ đảm nhận toàn bộ quá trình thiết kế, phát triển và quản lý website, giúp khách hàng tiết kiệm thời gian và chi phí.
	[b]Hỗ trợ khách hàng chuyên nghiệp:[/b] Cánh Cam luôn sẵn sàng hỗ trợ khách hàng mọi lúc mọi nơi, đảm bảo website của khách hàng luôn hoạt động ổn định.
	[b]Tại sao chọn Cánh Cam?[/b]
	[b]Đội ngũ chuyên nghiệp, giàu kinh nghiệm:[/b] Cánh Cam sở hữu đội ngũ nhân viên thiết kế website chuyên nghiệp, giàu kinh nghiệm, am hiểu về SEO và marketing online.
	[b]Cam kết chất lượng:[/b] Cánh Cam cam kết mang đến cho khách hàng website chất lượng cao, đáp ứng mọi yêu cầu của khách hàng.
	[b]Giá cả cạnh tranh:[/b] Cánh Cam cung cấp dịch vụ thiết kế website với mức giá cạnh tranh, phù hợp với mọi đối tượng khách hàng.
	[b]Liên hệ với Cánh Cam ngay hôm nay để được tư vấn và nhận báo giá thiết kế website:[/b]
[b]Website:[/b] [Website của Cánh Cam]
[b]Email:[/b] [Email của Cánh Cam]
[b]Số điện thoại:[/b] [Số điện thoại của Cánh Cam]
Hãy để Cánh Cam giúp bạn xây dựng website chuyên nghiệp, hiệu quả, nâng tầm thương hiệu và đạt được thành công trong kinh doanh online.''',
    'tags': 'tag1, tag2, tag3',  # Separate tags by commas
    'watch_thread': '0',  # Optionally, set to '1' to watch the thread
    'watch_thread_email': '0',  # Optionally, set to '1' to receive email notifications
    # Add other form fields and their values as needed
    # Be sure to include any hidden fields such as _xfToken
    '_xfRelativeResolver': 'https://lumanager.net/forums/rao-vat-dich-vu-khac.40/create-thread',
    '_xfToken': token
}


response = session.post(url, data=form_data,cookies=cookie)
redirect_url = response.headers.get('location')
print(redirect_url)


result.write(response.text)



# import google.generativeai as genai
# import os

# genai.configure(api_key=os.environ["AIzaSyAUYOLZuRdh_yYvNzBq0Q0BLsC8Ba9J_sE"])

# model = genai.GenerativeModel("gemini-1.0-pro")



# import genai

# # Replace with your actual Gemini API key
# gemini_api_key = "AIzaSyAUYOLZuRdh_yYvNzBq0Q0BLsC8Ba9J_sE"

# # Configure the client with your API key
# client = genai.Clients.TextGeneration(api_key=gemini_api_key)




session.close()



