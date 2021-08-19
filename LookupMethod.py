# Lookup value comparison
class LookupValidation:

    def __init__(self, expected_lookup, actual_lookup):
        self.expected_lookup = expected_lookup
        self.actual_lookup = actual_lookup

    def lookup_validate(self):

        lookup_mismatch_flag = 0

        length_expected = len(self.expected_lookup)
        length_actual = len(self.actual_lookup)

        if length_expected == length_actual:
            for index in range(length_expected):
                if self.expected_lookup[index] != self.actual_lookup[index]:
                    lookup_mismatch_flag += 1

            if lookup_mismatch_flag == 0:
                print('Lookup values matches with requirement')

            else:
                print('Lookup values are not matching with requirement')
        else:
            print('Lookup count is not matching with requirement')


Industry_Lookup_Expected = ['Agriculture', 'Education', 'Healthcare', 'IT', 'Unemployed', 'Retired', 'Other']
Industry_Lookup_Actual = ['Agriculture', 'Education', 'Healthcare', 'IT', 'Unemployed', 'Retired', 'Other']

Industry_Lookup = LookupValidation(Industry_Lookup_Expected, Industry_Lookup_Actual)
Industry_Lookup.lookup_validate()
