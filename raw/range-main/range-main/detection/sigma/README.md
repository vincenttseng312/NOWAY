# detection/sigma/

十一類鑑識點的 Sigma 規則。**規則與引擎解耦、產品無關**——Phase 1 在 Wazuh / Zircolite
上驗證，可移植到任何支援 Sigma 的偵測引擎。

## 對映（待落地）

- 三條 TTP 見 [SPEC §6](../../docs/SPEC.md)；**十一類鑑識點 → sensor/logsource 的施作清單見
  [SPEC §7](../../docs/SPEC.md)**（每類要寫成哪種 logsource、由哪個 sensor 守，那張表就是規格）。
- 各 atomic / GOAD 攻擊路徑與十一類鑑識點、三條 TTP 的逐項對映尚未比對（見 SPEC §11 開放項）。

## Phase 1 流程

跑一條 TTP（建議先 TTP1 竊密鏈）→ 錄 artifact → 把十一類鑑識點逐條寫成 Sigma →
在 Wazuh / Zircolite 上驗證 → 進擴充四態評分表（[SPEC §9](../../docs/SPEC.md)）。
