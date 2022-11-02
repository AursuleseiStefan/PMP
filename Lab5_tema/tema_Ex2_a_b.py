import pgmpy
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

if __name__ == '__main__':
    game_model = BayesianNetwork(
        [
            ("CJ1", "CJ2"),
            ('CJ1', 'D1'),
            ("CJ2", "D2"),
            ("D1", "D2"),
            ("D2", "D3"),
            ("CJ1", "D3")
        ]
    )

    cpd_cj1 = TabularCPD('CJ1', 5, [[0.2], [0.2], [0.2], [0.2], [0.2]],
                         state_names={
                                        'CJ1': ['AsF', 'RegeF', 'RegeI', 'ReginaF', 'ReginaI']
                                    })
    cpd_cj2 = TabularCPD(variable='CJ2',
                         variable_card=5,
                         values=[[0.0, 0.25, 0.25, 0.25, 0.25],
                                 [0.25, 0.0, 0.25, 0.25, 0.25],
                                 [0.25, 0.25, 0.0, 0.25, 0.25],
                                 [0.25, 0.25, 0.25, 0.0, 0.25],
                                 [0.25, 0.25, 0.25, 0.25, 0.0]],
                         evidence=['CJ1'],
                         evidence_card=[5],
                         state_names={
                             'CJ2': ['AsF', 'RegeF', 'RegeI', 'ReginaF', 'ReginaI'],
                             "CJ1": ['AsF', 'RegeF', 'RegeI', 'ReginaF', 'ReginaI']
                             })
    cpd_d1 = TabularCPD(variable='D1',
                        variable_card=2,
                        values=[[1, 0.75, 0.5, 0.25, 0.0],  # pariaza
                                [0.0, 0.25, 0.5, 0.75, 1]],  # asteapta
                        evidence=['CJ1'],
                        evidence_card=[5],
                        state_names={
                            'D1': ['Pariaza', 'Asteapta'],
                            'CJ1': ['AsF', 'RegeF', 'RegeI', 'ReginaF', 'ReginaI']
                        })
    cpd_d2 = TabularCPD(variable='D2',
                        variable_card=3,
                        values=[[1, 1, 0.75, 0.75, 0.5, 0.5, 0.25, 0.25, 0.0, 0.0],  # pariaza
                                [0.0, 0.0, 0.0, 0.25, 0.0, 0.5, 0.0, 0.75, 0.0, 1],  # asteapta
                                [0.0, 0.0, 0.25, 0.0, 0.5, 0.0, 0.75, 0.0, 1, 0.0]],  # iese din joc
                        evidence=['CJ2', 'D1'],
                        evidence_card=[5, 2],
                        state_names={
                            'D2': ['Pariaza', 'Asteapta', 'Afara'],
                            'CJ2': ['AsF', 'RegeF', 'RegeI', 'ReginaF', 'ReginaI'],
                            'D1': ['Pariaza', 'Asteapta']
                        })
    cpd_d3 = TabularCPD(variable='D3',
                        variable_card=2,
                        values=[[1, 1, 1, 0.75, 0.75, 0.75, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.0, 0.0, 0.0],  # pariaza
                                [0.0, 0.0, 0.0, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 1, 1, 1]],  # iese din joc
                        evidence=['CJ1', 'D2'],
                        evidence_card=[5, 3],
                        state_names={
                            'D3': ['Pariaza', 'Afara'],
                            'CJ1': ['AsF', 'RegeF', 'RegeI', 'ReginaF', 'ReginaI'],
                            'D2': ['Pariaza', 'Asteapta', 'Afara']
                        })
    game_model.add_cpds(cpd_cj1, cpd_cj2, cpd_d1, cpd_d2, cpd_d3)

    # cerinta 2
    rez = VariableElimination(game_model)
    print("Raspuns subpunctul (a):\n", rez.query(['D1'], evidence={'CJ1': 'RegeF'}))
    print("Raspuns subpunctul (b):\n", rez.query(['D2'], evidence={'CJ2': 'RegeI', 'D1': 'Pariaza'}))