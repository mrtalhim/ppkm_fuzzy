import simpful as sf

FS = sf.FuzzySystem(show_banner=False)

tfs_new_cases = [sf.TriangleFuzzySet(0,0,20, term='ct1'),
                 sf.TriangleFuzzySet(0,20,50, term='ct2'),
                 sf.TriangleFuzzySet(20,50,150, term='ct3'),
                 sf.TriangleFuzzySet(50,150,150, term='ct4'),
                 ]

FS.add_linguistic_variable("new_cases",
                           sf.LinguisticVariable(tfs_new_cases,
                                                 universe_of_discourse=[0, 150])
                           )

tfs_hospitalization = [sf.TriangleFuzzySet(0,0,5, term='ct1'),
                       sf.TriangleFuzzySet(0,5,10, term='ct2'),
                       sf.TriangleFuzzySet(5,10,30, term='ct3'),
                       sf.TriangleFuzzySet(10,30,30, term='ct4'),
                       ]

FS.add_linguistic_variable("hospitalization_rate",
                           sf.LinguisticVariable(tfs_hospitalization,
                                                 universe_of_discourse=[0, 30])
                           )

tfs_mortality = [sf.TriangleFuzzySet(0,0,1, term='ct1'),
                 sf.TriangleFuzzySet(0,1,2, term='ct2'),
                 sf.TriangleFuzzySet(1,2,5, term='ct3'),
                 sf.TriangleFuzzySet(2,5,5, term='ct4')
                 ]

FS.add_linguistic_variable("mortality",
                           sf.LinguisticVariable(tfs_mortality,
                                                 universe_of_discourse=[0, 5])
                           )

tfs_testing = [sf.TriangleFuzzySet(0, 0, 5, term='memadai'),
               sf.TriangleFuzzySet(0, 5, 15, term='sedang'),
               sf.TriangleFuzzySet(5, 15, 100, term='terbatas')
               ]

FS.add_linguistic_variable("testing",
                           sf.LinguisticVariable(tfs_testing,
                                                 universe_of_discourse=[0, 100])
                           )

tfs_tracing = [sf.TriangleFuzzySet(0, 0, 5, term='terbatas'),
               sf.TriangleFuzzySet(0, 5, 14, term='sedang'),
               sf.TriangleFuzzySet(5, 14, 14, term='memadai')
               ]

FS.add_linguistic_variable("tracing_ratio",
                           sf.LinguisticVariable(tfs_testing,
                                                 universe_of_discourse=[0, 14])
                           )

tfs_bor = [sf.TriangleFuzzySet(0, 0, 60, term='memadai'),
           sf.TriangleFuzzySet(0, 60, 80, term='sedang'),
           sf.TrapezoidFuzzySet(60, 80, 100, 100, term='terbatas')
           ]

FS.add_linguistic_variable("bed_occupancy_rate",
                           sf.LinguisticVariable(tfs_bor,
                                                 universe_of_discourse=[0, 100])
                           )

FS.set_crisp_output_value('level_1', 1)
FS.set_crisp_output_value('level_2', 2)
FS.set_crisp_output_value('level_3', 3)
FS.set_crisp_output_value('level_4', 4)

rules = [
    "IF (hospitalization_rate IS ct1) OR (mortality IS ct1) OR (new_cases IS ct1) OR (testing IS memadai) OR (tracing_ratio IS memadai) OR (bed_occupancy_rate IS memadai) THEN (ppkm IS level_1)",
    "IF (hospitalization_rate IS ct1) OR (mortality IS ct1) OR (new_cases IS ct1) OR (testing IS sedang) OR (tracing_ratio IS sedang) OR (bed_occupancy_rate IS sedang) THEN (ppkm IS level_2)",
    "IF (hospitalization_rate IS ct1) OR (mortality IS ct1) OR (new_cases IS ct1) OR (testing IS terbatas) OR (tracing_ratio IS terbatas) OR (bed_occupancy_rate IS terbatas) THEN (ppkm IS level_2)",
    "IF (hospitalization_rate IS ct2) OR (mortality IS ct2) OR (new_cases IS ct2) OR (testing IS memadai) OR (tracing_ratio IS memadai) OR (bed_occupancy_rate IS memadai) THEN (ppkm IS level_2)",
    "IF (hospitalization_rate IS ct2) OR (mortality IS ct2) OR (new_cases IS ct2) OR (testing IS sedang) OR (tracing_ratio IS sedang) OR (bed_occupancy_rate IS sedang) THEN (ppkm IS level_2)",
    "IF (hospitalization_rate IS ct2) OR (mortality IS ct2) OR (new_cases IS ct2) OR (testing IS terbatas) OR (tracing_ratio IS terbatas) OR (bed_occupancy_rate IS terbatas) THEN (ppkm IS level_3)",
    "IF (hospitalization_rate IS ct3) OR (mortality IS ct3) OR (new_cases IS ct3) OR (testing IS memadai) OR (tracing_ratio IS memadai) OR (bed_occupancy_rate IS memadai) THEN (ppkm IS level_2)",
    "IF (hospitalization_rate IS ct3) OR (mortality IS ct3) OR (new_cases IS ct3) OR (testing IS sedang) OR (tracing_ratio IS sedang) OR (bed_occupancy_rate IS sedang) THEN (ppkm IS level_3)",
    "IF (hospitalization_rate IS ct3) OR (mortality IS ct3) OR (new_cases IS ct3) OR (testing IS terbatas) OR (tracing_ratio IS terbatas) OR (bed_occupancy_rate IS terbatas) THEN (ppkm IS level_3)",
    "IF (hospitalization_rate IS ct4) OR (mortality IS ct4) OR (new_cases IS ct4) OR (testing IS memadai) OR (tracing_ratio IS memadai) OR (bed_occupancy_rate IS memadai) THEN (ppkm IS level_3)",
    "IF (hospitalization_rate IS ct4) OR (mortality IS ct4) OR (new_cases IS ct4) OR (testing IS sedang) OR (tracing_ratio IS sedang) OR (bed_occupancy_rate IS sedang) THEN (ppkm IS level_3)",
    "IF (hospitalization_rate IS ct4) OR (mortality IS ct4) OR (new_cases IS ct4) OR (testing IS terbatas) OR (tracing_ratio IS terbatas) OR (bed_occupancy_rate IS terbatas) THEN (ppkm IS level_4)",
	]

FS.add_rules(rules)

input = {
         'new_cases':8.57,
         'hospitalization_rate':.48,
         'mortality':1.48,
         'testing':1.77,
         'tracing_ratio':3.5,
         'bed_occupancy_rate':8.12
         }

for label, data in input.items():
    FS.set_variable(label, data)

output = FS.inference(['ppkm'], verbose=True)
output = round(output['ppkm'])
output = 'level {}'.format(output)
print(output)