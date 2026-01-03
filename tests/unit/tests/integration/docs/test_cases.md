# Login Test Cases

| Test Case ID | Description | Pre-condition | Input | Steps | Expected Result |
|-------------|------------|---------------|-------|-------|----------------|
| TC-01 | Valid login | User exists | admin/admin123 | Enter credentials | Login success |
| TC-02 | Valid format login | User exists | admin/admin123 | Login | Success |
| TC-03 | Login after logout | User exists | admin/admin123 | Login | Success |
| TC-04 | System available | User exists | admin/admin123 | Login | Success |
| TC-05 | Invalid password | User exists | admin/wrong | Login | Fail |
| TC-06 | Empty fields | None | empty | Login | Error |

