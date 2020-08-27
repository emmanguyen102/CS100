study_benefit = float(input("Enter the amount of the study benefits: "))
index_raise = 1.0117
study_benefit_after_raise = float(study_benefit * index_raise)
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", study_benefit_after_raise, "euros")
another_raise = float(study_benefit_after_raise * index_raise)
print("and if there was another index raise, the study")
print("benefits would be as much as", another_raise, "euros")