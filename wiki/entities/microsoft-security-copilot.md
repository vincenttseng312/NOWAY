---
type: entity
title: "Microsoft Security Copilot"
tags: [ai-security, security-tools, soc]
sources: [ai-security-tools-research-2026-07-16]
created: 2026-07-16
updated: 2026-07-16
---

# Microsoft Security Copilot

## 工具簡介

Microsoft Security Copilot 是面向安全與 IT 團隊的雲端生成式 AI 服務。它可在獨立介面，或 Defender XDR、Microsoft Sentinel、Intune、Entra 等 Microsoft 安全產品的嵌入式體驗中使用，協助警報調查、KQL、惡意腳本理解、風險管理、政策與報告。

它最適合已經使用 Microsoft Security 生態、具有正確 RBAC 與可靠資料來源的組織。不適合當作 Wazuh lab 的即插即用元件，也不能取代事件證據、SOC 分析師、最小權限或事件應變流程。與自建 [[ai-analysis-pipeline]] 相比，Security Copilot 提供的是 Microsoft 產品內的服務與治理；自建流程則必須自己處理 Wazuh 資料映射、RAG、權限與 guardrail。

## 核心功能與運作原理

```text
Defender / Sentinel / Intune / Entra 資料與權限
        ↓
Security Copilot workspace、plugins、agents
        ↓
自然語言提示、KQL、事件關聯與分析草稿
        ↓
分析師回查原始證據、決定處置與產出報告
```

Copilot 不會越過使用者在 Microsoft 產品中既有的存取權。這是安全優點也是設計限制：如果使用者沒有正確角色、資料來源沒有接入，或資料本身品質不佳，AI 不能補足這些缺口。

## 適用情境

1. Defender XDR 或 Sentinel 的分析師要將複雜事件轉成有證據、可閱讀的調查摘要。
2. 團隊需要從自然語言起草 KQL，再由分析師審查查詢邏輯與結果。
3. 管理者需要以不同受眾語氣彙整風險、開放問題與保護措施。

## Onboarding 前準備

- 僅適用於 Microsoft 商業雲；官方文件目前不支援 GCC、GCC High、DoD 與 Azure Government 客戶。
- 先確認租戶屬於 Microsoft 365 E5 Security Copilot included，或需手動佈建 Security Compute Units (SCUs) 的類型；兩者 onboarding 路徑不同。
- 非 E5 included 的租戶需要 Azure subscription、適當 Entra/Purview 角色與 SCU 容量。SCU 以小時計費，必須先設定預算與使用量監控。
- 權限應用 Entra security group 管理，而不是為了使用 Copilot 而把所有人加入 Security Administrator。

官方資料：[Get started](https://learn.microsoft.com/en-us/copilot/security/get-started-security-copilot)、[manual onboarding](https://learn.microsoft.com/en-us/copilot/security/manual-onboarding)、[authentication and roles](https://learn.microsoft.com/en-us/copilot/security/authentication)。

## Windows PowerShell 說明

Security Copilot 是 tenant 層級雲端服務，沒有可在個人 Windows 主機用 PowerShell 安裝的 client package。Onboarding 應在 `https://securitycopilot.microsoft.com` 或 Azure portal 依官方步驟完成；不要下載名稱相似的非官方 PowerShell 模組。

PowerShell 在這個工具的正確角色是：你已擁有對應 Microsoft 服務與權限時，用於查詢或驗證資料來源，而不是跳過 SCU、RBAC 或 Workspace onboarding。任何 Microsoft Graph、Az 或 Sentinel 指令都應在該服務自己的官方文件與測試租戶中另行驗證。

## 快速開始：最小安全工作流

1. 確認授權類型與成本責任人，再建立或確認 Security Copilot workspace。
2. 以 security group 指派 Owner/Contributor，避免直接給所有使用者高權限 Entra 角色。
3. 確認 Defender/Sentinel 等資料來源與使用者的既有權限。
4. 用一個已知、非敏感的歷史警報提出可稽核問題，例如：

```text
請依事件中的證據整理時間軸，列出受影響帳號與主機。
若資料不足，請明確列出缺少的欄位；不要推測未出現的 IP、規則或 MITRE 技術。
```

5. 回查每個摘要項目對應的原始事件與查詢結果，再決定是否建立 incident、執行處置或輸出報告。

以上為文件化流程，沒有可用 tenant、SCU 或權限可供本機驗證。

## 設定、成本與安全實務

- 把 workspace、role assignment、資料分享選項與 SCU/overage 變更納入變更管理與稽核。
- 將使用量 dashboard 納入成本監控；第一次探索應採小範圍、受控的 prompts 和資料來源。
- 依職務設定 Defender、Sentinel、Intune 與 Entra 的服務角色；Copilot role 不是這些後端資料權限的替代品。
- 報告或 promptbook 應明確要求引用事件證據、標示不確定性與人工決策點，呼應 [[citation-hallucination-rules]] 的可追溯原則。

## 常見操作

| 操作 | 用途 | 驗證方式 |
|---|---|---|
| 建立 workspace / capacity | 建立 tenant 範圍的使用空間與 SCU | Azure/portal 顯示部署完成與預算設定。 |
| Role assignment | 指派 Owner/Contributor | 用 security group 測試最小可用權限。 |
| Standalone prompt | 對事件提出分析問題 | 每項結論可回查原始資料。 |
| Embedded experience | 在 Defender/Sentinel 等產品中使用 | 使用者同時具備服務本身的資料權限。 |

## 常見錯誤與排解

### 無法進入或看不到資料

先區分「沒有 Copilot Contributor/Owner」與「沒有 Defender/Sentinel/Intune/Entra 資料權限」。前者在 Copilot role assignment 處理，後者在各服務的 RBAC 處理；不要為了排錯直接授予 Global Administrator。

### Onboarding 時沒有適用容量選項

重新確認租戶的 E5 included 狀態、Azure subscription、resource group 與 SCU 佈建角色。非 E5 included 客戶需要 SCU；建立 capacity 後即可能開始計費，先確認預算與 overage 設定。

### AI 摘要看似合理但沒有證據

要求回覆列出資料來源與未知欄位，並由分析師在原始事件/查詢中驗證。將此情況當成提示品質、資料品質或存取權設計問題，而不是直接採用結論。

## 工具比較與重點整理

| 工具 | 強項 | 限制 | 對本專題定位 |
|---|---|---|---|
| Microsoft Security Copilot | Microsoft SOC/IT 整合、權限與工作流 | 依賴授權、SCU、資料來源和 RBAC | 企業參考架構。 |
| [[garak]] | AI/RAG/agent 測試 | 不提供 Microsoft 事件工作流 | 自建 AI 助理的安全測試。 |
| [[lakera-guard]] | AI 執行期防護 | 不做 Sentinel/Defender 調查 | 自建助理處理真實資料後的選項。 |

完成本頁後，應能正確判斷 Security Copilot 是否符合租戶條件、知道它沒有本機 PowerShell 安裝流程、用最小權限建立 workspace，並要求所有 AI 調查結果回查原始證據。

## 關聯

- 來源：[[ai-security-tools-research-2026-07-16]]
- 選型與盤點：[[ai-security-tool-selection]]、[[wiki-content-strengthening-audit-2026-07-16]]
- 專題流程：[[ai-analysis-pipeline]]、[[citation-hallucination-rules]]
