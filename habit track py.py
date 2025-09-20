import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌀 30 Günlük Alışkanlık Değişim Takibi")

# Kullanıcıdan bilgiler
bad_habit = st.text_input("❌ Bırakmak istediğin alışkanlık:")
new_habit = st.text_input("✅ Yerine koymak istediğin davranış:")

if bad_habit and new_habit:
    st.write(f"Plan: **{bad_habit}** bırakılıyor ve yerine **{new_habit}** geliyor 🚀")

    # Başlangıç tarihi
    start_date = st.date_input("Başlangıç tarihi", datetime.date.today())

    # 30 günlük tarih listesi
    days = [(start_date + datetime.timedelta(days=i)) for i in range(30)]

    # Session state ile ilerleme kaydı
    if "progress" not in st.session_state:
        st.session_state.progress = {str(day): False for day in days}

    # Günlük işaretleme
    st.subheader("📅 Günlük Takip")
    for day in days:
        checked = st.checkbox(str(day), value=st.session_state.progress[str(day)])
        st.session_state.progress[str(day)] = checked

    # Rapor
    done_days = sum(st.session_state.progress.values())
    progress_percent = (done_days / 30) * 100

    st.subheader("📊 Rapor")
    st.write(f"✔ Tamamlanan gün: {done_days}/30")
    st.progress(progress_percent / 100)

    # Grafik
    st.subheader("📈 İlerleme Grafiği")
    progress_data = pd.DataFrame({
        "Gün": list(range(1, 31)),
        "Tamamlandı": [1 if st.session_state.progress[str(d)] else 0 for d in days]
    })

    plt.figure(figsize=(8, 4))
    plt.plot(progress_data["Gün"], progress_data["Tamamlandı"].cumsum(), marker="o")
    plt.xlabel("Gün")
    plt.ylabel("Toplam İlerleme")
    plt.title("30 Günlük İlerleme Grafiği")
    st.pyplot(plt)

    # 30 gün bittiğinde mesaj
    if done_days == 30:
        st.success("🎉 Tebrikler! 30 gün boyunca yeni alışkanlığını sürdürdün!")
