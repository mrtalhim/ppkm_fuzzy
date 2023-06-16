import simpful as sf

FS = sf.FuzzySystem(show_banner=False)

tfs_new_cases = [sf.FuzzySet([[0, 1],[20, 0]], term='ct1'),
                 sf.TriangleFuzzySet(0,20,50, term='ct2'),
                 sf.TriangleFuzzySet(20,50,150, term='ct3'),
                 sf.FuzzySet([[50, 0], [150, 1]], term='ct4'),
                 ]

FS.add_linguistic_variable("new_cases",
                           sf.LinguisticVariable(tfs_new_cases,
                                                 universe_of_discourse=[0, 150])
                           )

tfs_hospitalization = [sf.FuzzySet([[0, 1], [5, 0]], term='ct1'),
                       sf.TriangleFuzzySet(0,5,10, term='ct2'),
                       sf.TriangleFuzzySet(5,10,30, term='ct3'),
                       sf.FuzzySet([[10, 0],[30, 1]], term='ct4'),
                       ]

FS.add_linguistic_variable("hospitalization_rate",
                           sf.LinguisticVariable(tfs_hospitalization,
                                                 universe_of_discourse=[0, 30])
                           )

tfs_mortality = [sf.FuzzySet([[0, 1], [1, 0]], term='ct1'),
                 sf.TriangleFuzzySet(0,1,2, term='ct2'),
                 sf.TriangleFuzzySet(1,2,5, term='ct3'),
                 sf.FuzzySet([[2, 0],[5, 1]], term='ct4')
                 ]

FS.add_linguistic_variable("mortality",
                           sf.LinguisticVariable(tfs_mortality,
                                                 universe_of_discourse=[0, 5])
                           )

tfs_testing = [sf.FuzzySet([[0, 1], [5, 0]], term='memadai'),
               sf.TriangleFuzzySet(0, 5, 15, term='sedang'),
               sf.FuzzySet([[5, 0], [100, 1]], term='terbatas')
               ]

FS.add_linguistic_variable("testing",
                           sf.LinguisticVariable(tfs_testing,
                                                 universe_of_discourse=[0, 100])
                           )

tfs_tracing = [sf.FuzzySet([[0, 1], [5, 0]], term='terbatas'),
               sf.TriangleFuzzySet(0, 5, 14, term='sedang'),
               sf.FuzzySet([[5, 0], [14, 1]], term='memadai')
               ]

FS.add_linguistic_variable("tracing_ratio",
                           sf.LinguisticVariable(tfs_testing,
                                                 universe_of_discourse=[0, 14])
                           )

tfs_bor = [sf.FuzzySet([[0, 1], [60, 0]], term='memadai'),
           sf.TriangleFuzzySet(0, 60, 80, term='sedang'),
           sf.TrapezoidFuzzySet(60, 80, 100, 100, term='terbatas')
           ]

FS.add_linguistic_variable("bed_occupancy_rate",
                           sf.LinguisticVariable(tfs_bor,
                                                 universe_of_discourse=[0, 100])
                           )

# FS.set_crisp_output_value('level_1', 25)
# FS.set_crisp_output_value('level_2', 50)
# FS.set_crisp_output_value('level_3', 75)
# FS.set_crisp_output_value('level_4', 100)

lv_ct = sf.AutoTriangle(4, terms=['ct1', 'ct2', 'ct3', 'ct4'],
                         universe_of_discourse=[0, 1])

FS.add_linguistic_variable("ct_level",
                           lv_ct
                           )

lv_response = sf.AutoTriangle(3, terms=['memadai', 'sedang', 'terbatas'],
                              universe_of_discourse=[0, 1])

FS.add_linguistic_variable("response",
                           lv_response
                           )

ct_rules = [
    "IF (hospitalization_rate IS ct1) OR (mortality IS ct1) OR (new_cases IS ct1) THEN (ct_level IS ct1)",
    "IF (hospitalization_rate IS ct2) OR (mortality IS ct2) OR (new_cases IS ct2) THEN (ct_level IS ct2)",
    "IF (hospitalization_rate IS ct3) OR (mortality IS ct3) OR (new_cases IS ct3) THEN (ct_level IS ct3)",
    "IF (hospitalization_rate IS ct4) OR (mortality IS ct4) OR (new_cases IS ct4) THEN (ct_level IS ct4)",
	]

FS.add_rules(ct_rules)

response_rules = [
    "IF (testing IS memadai) OR (tracing_ratio IS memadai) OR (bed_occupancy_rate IS memadai) THEN (response IS memadai)",
    "IF (testing IS sedang) OR (tracing_ratio IS sedang) OR (bed_occupancy_rate IS sedang) THEN (response IS sedang)",
    "IF (testing IS terbatas) OR (tracing_ratio IS terbatas) OR (bed_occupancy_rate IS terbatas) THEN (response IS terbatas)",
    ]

FS.add_rules(response_rules)

input = {
         'new_cases':153.62,
         'hospitalization_rate':0,
         'mortality':6.83,
         'testing':22.5,
         'tracing_ratio':0,
         'bed_occupancy_rate':7.14
         }

for label, data in input.items():
    FS.set_variable(label, data)

output = FS.inference()
# output = FS.inference(['ppkm'], verbose=True)
# output = round(output['ppkm'])
# output = 'level {}'.format(output)
print(output)