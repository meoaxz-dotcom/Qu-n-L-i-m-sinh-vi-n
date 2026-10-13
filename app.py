import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Ứng dụng Quản lý và Thống kê Điểm Sinh viên")

data = {
    'họ và tên': [
        'Mộc Miên', 'Lê Gia Vũ', 'Băng Phong', 'Trầm Lam', 'Hoàng Nhật Thiên',
        'Diệp Khai', 'Tuệ An', 'Dịch Thần', 'Liên Hoa', 'Bách Uy'
    ],
    'Điểm chuyên cần': [8.0, 7.5, 6.0, 9.0, 7.0, 5.5, 8.5, 6.5, 7.5, 9.0],
    'Điểm giữa kỳ': [7.5, 8.0, 6.5, 8.5, 7.0, 6.0, 8.0, 7.0, 7.0, 9.0],
    'Điểm cuối kỳ': [7.0, 8.0, 7.0, 9.0, 7.5, 5.5, 8.5, 7.0, 7.5, 9.0]
}

df_sinhvien = pd.DataFrame(data)

df_sinhvien['Tong_ket'] = (
    0.2 * df_sinhvien['Điểm chuyên cần'] + 
    0.3 * df_sinhvien['Điểm giữa kỳ'] + 
    0.5 * df_sinhvien['Điểm cuối kỳ']
)

def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df_sinhvien['Xep_loai'] = df_sinhvien['Tong_ket'].apply(xep_loai)

st.subheader("Danh sách điểm sinh viên")
st.dataframe(df_sinhvien)

st.subheader("Thống kê kết quả")
diem_tb_lop = df_sinhvien['Tong_ket'].mean()
st.write(f"- Điểm tổng kết trung bình của lớp: **{diem_tb_lop:.2f}**")

sv_cao_nhat = df_sinhvien.loc[df_sinhvien['Tong_ket'].idxmax()]
st.write(f"- Sinh viên có điểm tổng kết cao nhất: **{sv_cao_nhat['họ và tên']}** ({sv_cao_nhat['Tong_ket']:.2f})")

sv_thap_nhat = df_sinhvien.loc[df_sinhvien['Tong_ket'].idxmin()]
st.write(f"- Sinh viên có điểm tổng kết thấp nhất: **{sv_thap_nhat['họ và tên']}** ({sv_thap_nhat['Tong_ket']:.2f})")

so_luong_dat = (df_sinhvien['Tong_ket'] >= 5.0).sum()
st.write(f"- Số sinh viên đạt (điểm tổng kết >= 5): **{so_luong_dat} / 10** sinh viên")

st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(df_sinhvien['họ và tên'], df_sinhvien['Tong_ket'], color='#5b9bd5')
ax.set_title('BIỂU ĐỒ ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN', fontsize=12, fontweight='bold')
ax.set_xlabel('Điểm tổng kết')
ax.set_ylabel('Tên sinh viên')
ax.invert_yaxis()
ax.grid(axis='x', linestyle='--', alpha=0.5)

st.pyplot(fig)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 12px; color: gray;'>"
    "Ứng dụng được thực hiện bởi: <b>Bùi Minh Đức</b> - MSSV: <b>024208006482</b>"
    "</p>", 
    unsafe_allow_html=True
)
