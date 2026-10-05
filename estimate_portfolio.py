import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("portfolio_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

completed_slugs = [
    "VƯƠNG HỔ ỨNG - LỤC HÀO NHẬP MÔN.pdf",
    "VƯƠNG HỔ ỨNG - KHÔNG VONG, NGUYỆT PHÁ, 12 CUNG TRƯỜNG SINH BÍ LUẬN.pdf",
    "VƯƠNG HỔ ỨNG - LỤC HÀO KỸ PHÁP VÀ ỨNG DỤNG.pdf",
    "VƯƠNG HỔ ỨNG - GIẢI ĐÁP NGHI VẤN TRONG TĂNG SAN BỐC DỊCH BÌNH THÍCH.pdf"
]

remaining = [b for b in manifest["books"] if b["file"] not in completed_slugs]

print(f"Tổng số cuốn còn lại: {len(remaining)} cuốn")
print("=" * 80)
total_est_min = 0

for i, b in enumerate(remaining, 1):
    pages = b["total_pages"]
    pairs = b["worker_pairs"]
    # Mỗi wave tối đa 80 pairs
    waves = (pairs + 79) // 80
    
    # Dự tính thời gian theo số wave thực tế:
    # - Rasterize: ~15s / 100 pages (~0.15s/trang)
    # - Worker wave: ~1.5 - 2 phút / wave (80 workers đồng thời)
    # - Stitch & Audit: ~1.5 phút
    t_rast = pages * 0.15 / 60.0
    t_workers = waves * 1.75
    t_audit = 1.2
    est_minutes = t_rast + t_workers + t_audit
    total_est_min += est_minutes
    
    print(f"{i:2d}. {b['file'][:45]:<45} | {pages:3d} tr | {pairs:3d} pairs | {waves} wave(s) | ~{est_minutes:.1f} phút")

print("=" * 80)
print(f"Tổng thời gian dự kiến cho toàn bộ 16 cuốn còn lại: ~{total_est_min:.0f} phút (~{total_est_min/60:.1f} giờ)")
