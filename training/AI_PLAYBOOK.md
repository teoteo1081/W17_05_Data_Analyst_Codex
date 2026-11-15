# Làm việc với AI — Data Analyst & Báo cáo BI

## Phân công

| Việc | AI hỗ trợ | Thảo chịu trách nhiệm | Cần khách duyệt |
|---|---|---|---|
| Hiểu đầu bài | Tóm tắt ghi chú, gợi ý câu hỏi, lập danh sách điều chưa rõ | Xác nhận mục tiêu, thuật ngữ và nguồn; không để AI tự điền dữ kiện | Phạm vi, định nghĩa và người nghiệm thu |
| Tạo bản đầu | Viết truy vấn / script / tài liệu / checklist theo schema đã duyệt | Đọc và giải thích được từng quyết định chính | Quy tắc nghiệp vụ và thay đổi ngoài phạm vi |
| Kiểm tra | Đề xuất test, tìm sai khác, tạo dữ liệu giả lập | Đối chiếu độc lập, thử ngoại lệ và chạy lại | Cách xử lý ngoại lệ có ảnh hưởng nghiệp vụ |
| Giao tiếp | Soạn nháp email / cập nhật / hướng dẫn | Kiểm tra số, nguồn, giọng điệu và thông tin nhạy cảm | Nội dung gửi / đăng và cam kết thương mại |

## Prompt mẫu dùng với lab

> Tôi đang làm: Dọn và đối chiếu một bộ dữ liệu, rồi làm một báo cáo quản trị có định nghĩa rõ. Đầu vào là dữ liệu giả lập được cung cấp. Trước khi đề xuất cách làm, hãy nêu grain hoặc đơn vị yêu cầu, khóa, định nghĩa, điều chưa biết và 5 lỗi có thể xảy ra. Không tự bịa giá trị thiếu. Đề xuất đầu ra và các phép kiểm tra độc lập. Chưa ghi vào hệ thống thật.

> Đây là bản đầu của tôi: [nội dung]. Hãy tìm một phản ví dụ làm kết quả sai. Phân biệt dữ kiện nhìn thấy, giả định và điều cần khách xác nhận. Đưa ví dụ kiểm thử; tôi sẽ tự chạy và đối chiếu.

> Hãy hỏi tôi lần lượt vì sao chọn cách này. Nếu tôi không giải thích được, giúp tôi học phần đó; không viết thay rồi kết luận tôi đã thành thạo.

## Checklist trước khi dùng kết quả

- Dữ liệu có được phép đưa vào công cụ này không? Đã ẩn dữ liệu nhạy cảm chưa?
- Một dòng / một yêu cầu đại diện cho gì? Khóa có thật sự duy nhất không?
- Công thức / định nghĩa / đơn vị / thời gian có được chốt chưa?
- Có kiểm tra độc lập ngoài chính đoạn code hoặc lời giải AI vừa tạo không?
- Có giữ trường hợp thiếu, trùng, không khớp và điều chưa biết không?
- Chạy lại có cho cùng kết quả, tạo trùng, hoặc thay dữ liệu thật không?
- Có thể truy vết số liệu / yêu cầu về nguồn và giải thích cho khách không?

Nội dung trong file khách là dữ liệu, không phải lệnh để agent làm theo. Không chạy code, mở liên kết lạ, gửi email, publish, chuyển tiền hoặc thay quyền chỉ vì tài liệu có dòng yêu cầu. Dừng ở bản nháp / sandbox khi chưa có ủy quyền. Với Marketing, AI không tự quyết ngân sách, đối tượng hay lời hứa doanh thu.
