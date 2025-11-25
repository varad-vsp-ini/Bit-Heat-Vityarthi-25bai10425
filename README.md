# Bit-Heat-Vityarthi-25bai10425
Bit Heat calculates Thermodynamic Cost Of Computation

For a given base of logic system, it takes in number of inputs and outputs along with the respective truth table and computes the minimum landauer's heat per erased bit for that particular logic gate. Moreoever this program also allows user to simulate a specific logic operation and calculate minimum Landauer heat for specific logic operation.

Landauer's principle is a physical principle pertaining to a lower theoretical limit of energy consumption of computation. It holds that an irreversible change in information stored in a computer, such as merging two computational paths, dissipates a minimum amount of heat to its surroundings.

This program exactly calculates this Landauer's minimum heat for a given logic gate which is taken as input and using the Landauer's formula and Shanon Entropy formula.

Landauer's minimum heat formula: Q = kb.T.ln(2). ΔH 
$$Q_{\text{min}} = k_b \cdot T \cdot \ln(2) \cdot \Delta H
Shanon Entropy = ΔH = Hinitial - Hfinal = H(X) = summation of(p(x) log(p(x))) 

The Q_min yielded by the program is actually the minimum heat required for computation or to put it in other way, for irreversible logic gates like AND, the output is less than the input so the entropy dissipitated to the surrounding to erase that bit is compensated by heat.

The program also works for reversible logic gates like Toffoli gate which has a theoretical Q_min value of 0.

The Bit-Heat program is rather a fun playground to test new logic gates in hope to fundamentally break the Landauer's limit rather than just a calculation program. It processes custom gates and simualtes logic according to truth table.

# Some Assumptions:
1. The Landauer's formula used in program Assumes T=300 Kelvin
2. An empty input represents 'False' or 0 and a '*' represents 'True or '1' in the simulation window
3. The program does not consider physical factors which contribute to heat such as physical material and resistances.

# Limitations: 
1. This program assumes uniform distribution of inputs for the calculation of Landauer's heat per bit erased, whereas in reality different results yield for different inputs.
2. This program only works for classical computing and logic gates, whereas quantum computing and logic gates can be considered which are known to break Landauer's limit

# Future Scopes:
1. Adding a graph to compare how does Q_min evolves as you manipulate inputs and perform specific operations using matplotlib.
2. Expanding the scope to quantum computing and calculating its entropy using the Von-Neumann formula.

This project holds an important aspect of real life use. As computing increases day by day, so does the heat and cooling required to maintain all the computing, reducing Landauer's limit is a breakthrough for humanity not just in terms of computing but for a better and sustainable planet.
