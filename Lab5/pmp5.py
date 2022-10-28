from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete.CPD import TabularCPD
jucatori = BayesianNetwork([('jucatori , 'carti'), ('decizii', 'carti')])
grades_cpd = TabularCPD('carti', 5, [[1,0,0,1,0,0],
                                      [0.5,0.5,0,0.5,0.5,0],
                                      [0.3,0.3,0.3,0.3,0.3,0.3],
                                      [0.5,0.5,0,0.5,0.5,0],
                                      [1,0,0,1,0,0]],
                        evidence=['juc', 'carti'], evidence_card=[2, 3])
student.add_cpds(grades_cpd)