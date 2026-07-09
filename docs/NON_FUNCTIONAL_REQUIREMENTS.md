# Non Functional Requirements

Version: 1.0

---

## NFR-001 Performance

System shall process live video in real time.

Target FPS:
Minimum: 15 FPS
Recommended: 20+ FPS

---

## NFR-002 Startup Time

Software shall start within 15 seconds.

---

## NFR-003 Reliability

System shall operate continuously for at least 8 hours without crashing.

Target:
99.5% uptime during loading.

---

## NFR-004 Camera Recovery

If a camera disconnects, the system shall reconnect automatically within 10 seconds.

---

## NFR-005 Offline Operation

All features shall work without internet.

Internet is only required for optional cloud synchronization.

---

## NFR-006 Data Safety

Critical events shall never be lost.

If power fails:
- Save current recordings
- Save current event
- Resume safely after restart

---

## NFR-007 Logging

Every important action shall be logged.

Examples:
- Camera connected
- Camera disconnected
- Loading started
- DONE detected
- Alarm triggered

---

## NFR-008 Security

Only authorized users can:
- Delete recordings
- Change settings
- Export reports

---

## NFR-009 Storage

Old recordings shall be deleted automatically based on configurable storage limits.

---

## NFR-010 Scalability

System shall support:

Current Version
- 4 Cameras

Future Version
- 16 Cameras

without architecture changes.

---

## NFR-011 Maintainability

Every module shall be independent.

Changing one module should not require changing unrelated modules.

---

## NFR-012 Accuracy

Bird Detection
Target Accuracy: >98%

OCR
Target Accuracy: >99.5%

Critical Event Detection
Target Accuracy: >99%

---

## NFR-013 Evidence

Every critical event shall automatically save:

- Timestamp
- Camera ID
- Event ID
- Video Clip
- Bird Count
- OCR Result

---

## NFR-014 User Experience

Dashboard shall display critical alerts within 2 seconds.

---

## NFR-015 Configuration

All cameras, thresholds and settings shall be configurable without changing source code.