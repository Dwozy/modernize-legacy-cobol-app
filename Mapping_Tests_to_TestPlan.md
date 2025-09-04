| Test Case ID | Description (TESTPLAN.md)                                      | Couverture par les tests Python                                                                                 | Catégorie de test      |
|--------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------|
| TC-1.1       | View Current Balance                                          | `test_initial_balance` (unit), `test_operation_total_reads_balance` (integration), `test_full_user_journey` (e2e), `test_cobol_vs_python_e2e` (e2e) | unit, integration, e2e |
| TC-2.1       | Credit Account with Valid Amount                              | `test_credit_valid_amount` (unit), `test_operation_credit_updates_balance` (integration), `test_full_user_journey` (e2e), `test_cobol_vs_python_e2e` (e2e), `test_main_calls_operation_credit` (integration) | unit, integration, e2e |
| TC-2.2       | Credit Account with Zero Amount                               | `test_credit_zero_amount` (unit), `test_operation_credit_updates_balance` (integration), `test_full_user_journey` (e2e), `test_cobol_vs_python_e2e` (e2e) | unit, integration, e2e |
| TC-2.3       | Credit Account with Amount Exceeding Max Balance (plafond)    | `test_credit_caps_balance_and_warns` (unit), `test_full_user_journey` (e2e), `test_cobol_vs_python_e2e` (e2e)   | unit, e2e              |
| TC-3.1       | Debit Account with Valid Amount                               | `test_debit_valid_amount` (unit), `test_operation_debit_updates_balance` (integration), `test_full_user_journey` (e2e), `test_cobol_vs_python_e2e` (e2e), `test_main_calls_operation_debit` (integration) | unit, integration, e2e |
| TC-3.2       | Debit Account with Amount Greater Than Balance                | `test_debit_insufficient_funds` (unit), `test_operation_debit_insufficient_funds` (integration), `test_debit_insufficient` (e2e), `test_cobol_vs_python_e2e` (e2e) | unit, integration, e2e |
| TC-3.3       | Debit Account with Zero Amount                                | `test_debit_zero_amount` (unit), `test_operation_debit_updates_balance` (integration), `test_full_user_journey` (e2e), `test_cobol_vs_python_e2e` (e2e) | unit, integration, e2e |
| TC-4.1       | Exit the Application                                          | `test_choice_4_exits` (unit), `test_menu_loop_exit` (unit), `test_full_user_journey` (e2e), `test_cobol_vs_python_e2e` (e2e) | unit, e2e              |
| TC-5.1       | Saisie montant (point/virgule, refus texte/négatif/etc.)      | `test_get_valid_amount_valid_cases` (unit), `test_get_valid_amount_invalid_cases` (unit)                        | unit                   |
| TC-6.1       | Dispatch menu/command handling                                | `test_choice_1_calls_total` (unit), `test_choice_2_calls_credit` (unit), `test_choice_3_calls_debit` (unit), `test_invalid_choice` (unit), `test_non_numeric_choice` (unit) | unit                   |
| TC-7.1       | DataStore initialisation and persistence                      | `test_initial_balance` (unit), `test_write_and_read_balance` (unit)                                             | unit                   |
| TC-8.1       | Main-operation integration                                    | `test_main_calls_operation_total` (integration), `test_main_calls_operation_credit` (integration), `test_main_calls_operation_debit` (integration) | integration            |

---

### Détail des nouveaux tests ajoutés

- **test_credit_caps_balance_and_warns** (unit) : vérifie que le solde est plafonné à 999999.99 et que le message d’avertissement s’affiche.
- **test_get_valid_amount_valid_cases** (unit) : vérifie que `get_valid_amount` accepte les montants valides (point, virgule, zéro, etc.).
- **test_get_valid_amount_invalid_cases** (unit) : vérifie que `get_valid_amount` refuse les entrées invalides (texte, négatif, vide, etc.) et redemande jusqu’à obtenir une valeur correcte.

---

### Légende des catégories

- **unit** : test unitaire (fonction ou classe isolée)
- **integration** : test d’intégration (plusieurs modules ensemble)
- **e2e** : test end-to-end (parcours utilisateur complet ou comparaison COBOL/Python)

---

### Nombre de tests par catégorie

- **unit** : 25 (18 main + 5 operation + 2 data)
- **integration** :  7 (4 operation_data + 3 main_operation)
- **e2e** :  (2 userInteraction + 1 cobol_vs_python)
  ### **Totale**: 35
---
