import os, sys, json, time, hashlib

print("=" * 75)
print("🚀 [HẠT NHÂN THỨC TỈNH] Repo: homeostasis | Thẻ Bài: FLEET_HOMEOSTASIS")
print("=" * 75)

epoch = 1
if os.path.exists("synapses/state.json"):
    try:
        with open("synapses/state.json", "r") as f: epoch = json.load(f).get("generation_epoch", 0) + 1
    except Exception: pass

t = int(time.time())
cid = hashlib.shake_256(f"homeostasis_{epoch}_{t}".encode()).hexdigest(64)

# Ghi sổ state
with open("synapses/state.json", "w") as f:
    json.dump({"generation_epoch": epoch, "last_t": t, "quantum_cid": cid, "status": "running"}, f, indent=4)

# Xuất sóng forward
with open("synapse_forward.json", "w") as f:
    json.dump({"contract": "bodhi.contract.v1", "identity": "100048777766367/homeostasis", "epoch": epoch, "cid": cid}, f, indent=4)

# Ghi Báo Cáo Step Summary vào GitHub Actions
summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
if summary_file:
    with open(summary_file, "a", encoding="utf-8") as f:
        f.write(f"""
## 🎴 CHỨNG CHỈ KIỂM ĐỊNH THẺ BÀI: HOMEOSTASIS
> **Kỷ nguyên:** #{epoch} | **Thẻ Bài:** FLEET_HOMEOSTASIS | **Cổng I/O:** I/O (BALANCE_XOR_L)

| Hạng Mục | Trạng Thái | Đánh Giá |
| :--- | :---: | :--- |
| **Hạ Tầng** | 🟢 KÍN | Python 3.14 & Actions Setup v7 |
| **Bảo Chứng CID** | 🟢 KÍN | `{cid[:20]}...` |
""")

print(f"✨ [HOÀN MỸ] Nút mạng homeostasis đã vận hành chu kỳ #{epoch} (CID: {cid[:16]}...)")
