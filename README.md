# Bit-Heat-Vityarthi-25bai10425
Bit Heat calculates Thermodynamic Cost Of Computation

# Description
For a given base of logic system, it takes in number of inputs and outputs along with the respective truth table and computes the minimum landauer's heat per erased bit for that particular logic gate. Moreoever this program also allows user to simulate a specific logic operation and calculate minimum Landauer heat for specific logic operation.

Landauer's principle is a physical principle pertaining to a lower theoretical limit of energy consumption of computation. It holds that an irreversible change in information stored in a computer, such as merging two computational paths, dissipates a minimum amount of heat to its surroundings.

This program exactly calculates this Landauer's minimum heat for a given logic gate which is taken as input and using the Landauer's formula and Shanon Entropy formula.

The Bit-Heat program is rather a fun playground to test new logic gates in hope to fundamentally break the Landauer's limit rather than just a calculation program. It processes custom gates and simualtes logic according to truth table.

# Working Principles
## The program utilizes 2 libraries
1. pandas: To simplify the work of calculating output frequencies from truth table using pandas `value_count()` method
2. math: To compute logarithms and natural logarithms

## The program takes input of 4 things
1. Base of logic system
2. Number of Inputs
3. Number of Outputs
4. The respective Truth Table iterated $Base^{no.of.inputs}$ times
taking in respectively number of inputs and outputs.

Number of inputs and outputs are stored in seprate variables.
The respective inputs and outputs are stored in separate lists
There is also a dictionary created called `TT` which maps the input as tuple to outputs which is used in the simulation mode

Similarly a dictionary is created and in this dictionary, the pandas `value_count()` and `to_dict()` methods are use to store the output and its freqeuncy as a `key : value` pair.

## The Program also uses certain known formulas to compute    

1. Landauer's minimum heat formula: $Q_{\min} = k_B T \ln(2) \Delta H$

$\Delta H$ in the equation is given by = $\Delta H = H_{\text{initial}} - H_{\text{final}}$
where $H$ using the Shanon Entropy formula 

2. Shanon Entropy Formula: $H = - \sum_{i} p_i \log_2 p_i$

Refering to the above formulas by default the program takes the $H_{\text{initial}}$ value from the variable which stores the number of inputs as for every n amount of information for a logic gate, it takes in n bits of information

$H_{\text{final}}$ is however calculated through shanon entropy formula, A for loop is iterated through the dictionary which stores the frequency of outputs and $p$ (Probability) is calculated as the value of dictionary (or the frequency of that output) divided by $Base^{no.of.inputs}$.

This $p$ is then plugged into the shanon entropy formula mentioned above and we get $H_{\text{final}}$

And then after calculation the $Q_{\min}$ is printed.

The $Q_{\min}$ yielded by the program is actually the minimum heat required for computation or to put it in other way, for irreversible logic gates like AND, the output is less than the input so the entropy dissipitated to the surrounding to erase that bit is compensated by heat.

Then the user is given a optional simulation mode, which when entered with yes, simulates the logic gate and it also returns the Landauer’s heat for each computation. Except the formula this time is
$Q_{\min} = k_B T \ln(2) \log_2 (p)$

where p = frequency of that output in the truth table.

The simulation mode works solely on basis of the truth table provided by user, first the false and true statements from user's logic is converted to " " or "*".
There exists extra variables or lists in this loop called rlinps rlouts which refer to real time inupts or real time outputs which is processed as the user enter input operations and program maps it to the output operations.

The Simulation mode simply utilizes the information stored in `TT` dictionary which has the truth table stored as `(input) : (output)` format.
The if else statements in the loop actively recognize and map the user input to one of the key of `TT` dictionary and displays the respective value. If A user enters any input operation that is not formerly in the truth table, the program displays error.

After each operation the $Q_{\min}$ value is printed for that specific operation using the formulas mentioned above.

The loop is terminated once the user enters `n` on choice

The program also works for reversible logic gates like Toffoli gate which has a theoretical $Q_{\min}$ value of 0.

# Some Assumptions:
1. The Landauer's formula used in program Assumes $T=300$ Kelvin
2. An empty input represents 'False' or 0 and a '*' represents 'True or '1' in the simulation window
3. The program does not consider physical factors which contribute to heat such as physical material and resistances.

# Limitations: 
1. This program assumes uniform distribution of inputs for the calculation of Landauer's heat per bit erased, whereas in reality different results yield for different inputs.
2. This program only works for classical computing and logic gates, whereas quantum computing and logic gates can be considered which are known to break Landauer's limit

# Future Scopes:
1. Adding a graph to compare how does $Q_{\min}$ evolves as you manipulate inputs and perform specific operations using matplotlib.
2. Expanding the scope to quantum computing and calculating its entropy using the Von-Neumann formula.

This project holds an important aspect of real life use. As computing increases day by day, so does the heat and cooling required to maintain all the computing, reducing Landauer's limit is a breakthrough for humanity not just in terms of computing but for a better and sustainable planet.
