# W17_05_Data_Analyst_Codex

**Thao Nguyen (TJ) — Data Analyst & Báo cáo BI. Codex phụ trách chính.**

Hồ sơ chào dịch vụ thật để trao đổi với khách và so sánh cách triển khai giữa các agent. Bộ học nằm riêng trong training/. Không đưa trạng thái học, bài làm hay điểm cá nhân lên giao diện bán dịch vụ.

## Bắt đầu

- Website: index.html (VI / EN / ES / ZH), dùng tài nguyên tĩnh trong assets/, không cần CDN.
- Gói đầu tiên đề xuất: **Dọn và đối chiếu một bộ dữ liệu, rồi làm một báo cáo quản trị có định nghĩa rõ**.
- Học: [training/START_HERE.md](training/START_HERE.md).
- Kịch bản khách: [training/CLIENT_PLAYBOOK.md](training/CLIENT_PLAYBOOK.md).
- Tiếp tục chấm bài ở phiên sau: [COACHING.md](COACHING.md).
- Bản kế hoạch so sánh: [docs/PROFILE_STRATEGY.md](docs/PROFILE_STRATEGY.md).

## Chạy và sửa

    python -m http.server 8000 --bind 127.0.0.1

Mở http://127.0.0.1:8000. Chỉnh nội dung trong profile.json và assets/site_ui.json, sau đó:

    python tools/build_site.py
    python tests/verify_profile.py

Thư mục này có Git mới hoàn toàn, main riêng, không có lịch sử hoặc runtime phụ thuộc W17_04 hay các profile khác. Không sao chép .git cũ. Cookie / browser storage có namespace theo tên folder. AGENTS.md giữ quy chuẩn chung; W17_04 được giữ nguyên.

## Dữ liệu và quyền riêng tư

Case trên website là dữ liệu giả lập, được ghi nhãn rõ; không phải số liệu hay lời chứng thực của khách. Không thêm số năm, bằng cấp, chứng nhận, doanh thu hoặc kết quả tiết kiệm chưa có bằng chứng. Phạm vi Marketing là vận hành / dữ liệu, không tự nhận KPI chiến lược hay chi quảng cáo.

training/submissions/, assessment_state.local.json và coach_answer_key.local.md được Git bỏ qua. Bài làm và điểm thật chỉ lưu cục bộ. File học công khai không chứa câu trả lời của Thảo. Không kết luận năng lực từ hồ sơ được sinh, câu hỏi mơ hồ hoặc bài có hướng dẫn.
