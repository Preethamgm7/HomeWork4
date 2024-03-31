# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "No"
    answers["(b)"] = "No"
    answers["(c)"] = "Yes"        
    answers["(d)"] = "Yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Rules are counting as conflicting if no given case (or instance) satisfies more than one rule together. Unfortunately, within this pool, the overlaps are likely to occur. In this case, a homeowner who satisfies rule (1) could also have downgraded annual income under rule (3) and he could be marked as the defaulted borrower (DB = Yes). This fact however does not make the rules mutually inconclusive because an individual's own attributes could be stimulators of many rules."
    answers["(b) explain"] = "Any rule which does not apply in an situation is called a mutually exclusive rule and, in that situation, a case (instance) cannot satisfy more than one rule. Here it is overlapping with another. Consequently, a Home Owner (H= Yes) might also be a person that has Low Annual Income (L= Yes), which means that the individual would fulfill both conditions that a defaulted borrower (DB = yes) should have. In this case, those rules may not be mutually exclusive as efforts of one individual can be guided by more than one rule."
    answers["(c) explain"] = "Therefore, because the rules are not independent, the order of them could be a factor in the final classification result. If a case falls under more than one rule, the order defines which of the rules takes effect first and therefore impacts the default borrower's final decision response. Ranking the rules ensure the uniformly fair results."
    answers["(d) explain"] = "The rule set is not complete excluding cases that do not conform to the presented rules. The classes are required to classify cases that are unmatched. The default class will be a catch-all classification making sure that all the cases will be possessed by this classification even if they don't fall under the specific rules. Lack of a default class will lead to the fact that some of the individuals will remain unclassified. That is undesirable in a rule-based system where the final purpose is to make the definite predictions."

    return answers


# -----------------------------------------------------------

def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = ""
    answers["(b)"] = ""
    answers["(c)"] = ""
    answers["(d)"] = ""

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers

# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "Yes"
    answers["(b)"] = "No"
    answers["(c)"] = "No"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Think of rules as guidelines that help us categorize different creatures. Imagine you have a bunch of cases, or examples of animals, and you want to sort them into groups. Each rule is like a special instruction for sorting. Let me put it in simpler terms: 1. Rule 1: If you see an animal that breathes air and doesn't give birth to babies, we'll call it a bird. 2. Rule 2: Now, if you come across a water creature with a backbone that doesn't lay eggs, we'll call it a fish. 3. Rule 3: Any warm-blooded creature is called a mammal. 4. Rule 4: If an animal gives birth to live babies, isn't a bird, and isn't a fish, it's a reptile. These rules are set up so that each one only applies to specific situations. They don't overlap because each rule looks for certain traits that are unique to it."
    answers["(b) example"] = "The guidelines will be incredibly detailed, covering every conceivable scenario. Each piece of information will be carefully examined, ensuring that it fits into at least one rule. However, these rules are not universal and may not apply in every situation. For instance, they don't explicitly address amphibians like salamanders, which are cold-blooded and give birth, or birds like penguins, which are warm-blooded but don't fly."
    answers["(c) example"] = "Because these reasons are separate and don't overlap, only one of them can apply to a specific situation. This means the order in which they're considered doesn't really make a difference. So, the process of sorting them isn't random at all. No matter the sequence, each reason will lead to the same categorization, just based on which rule is being followed. However, it's important to note that if a reason isn't listed, it might not get categorized at all, which is a separate concern from where the reasons fit into the rules."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "In simpler terms, when you're working with a deep learning network, imagine each layer as a step in a staircase. The 'gradient' is like the steepness of each step. Now, to make sure each step is just right, we use the gradient at one step to figure out how it affects the step before it. It's a bit like understanding how the angle of one step affects the angle of the step below it. This helps us adjust the 'weights' of each layer, kind of like fine-tuning each step so that the whole staircase leads us to the right answer.."
    answers["(b) explain"] = "When a neural network progresses from one layer to the next, it's like passing a message from one group of brain cells to the next. Each group of cells (or nodes) in the network has its own set of connections (or weights) to the next group. To activate the next group of cells, we sum up the inputs from the previous group, just like combining signals from different parts of the brain, and then apply a function to determine the final output."
    answers["(c) explain"] = "During training artificial neural networks (ANNs), there's this thing called the vanishing gradient problem. It's like when you're trying to teach something to someone, but the message gets lost along the way, especially when you're going back and forth. So, with ANNs, it's like the algorithm struggles to pass on the lessons it learned in the later stages to the earlier ones. It's not about forgetting what was taught, but more like struggling to pass on the knowledge effectively."
    answers["(d) explain"] = "Simply achieving flawless performance with Artificial Neural Networks (ANNs) doesn't guarantee that the gradients of the loss function concerning the weights in each layer will be uniformly zero. Attaining a global optimal minimum for the model requires zero gradients. However, even with perfect classification of the training set, the model may still possess non-zero gradients if it's specifically designed for the dataset, as the loss function typically accommodates some margin of error."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.28
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "No"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.4
    answers["(c) P(X_2=1 | +)"] = 0.4
    answers["(c) P(X_2=1 | -)"] = 0.5
    answers["(c) P(X_3=1 | +)"] = 0.16
    answers["(c) P(X_3=1 | -)"] = 0

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "The graph depicted in Figure KNN (a) illustrates clear clusters distinguished by different colors, indicating no overlap between classes. In such scenarios, opting for a small value of K is favored, as it ensures instances of each class are tightly grouped together in space. Specifically, when K = 1, performance tends to be slightly superior, as there are very few neighbors considered, minimizing the likelihood of misclassification. However, in cases where class separation is already well-defined, such as in scenario A, selecting a large value like K = 50 might overly smooth the decision boundary, making it less optimal as a primary choice."
    answers["(b) explain"] = "In Figure KNN (b), the plot illustrates significant overlap between classes, suggesting that individual instances may not accurately represent the overall class distribution due to noise or overlapping. To counteract the influence of noise, using a larger k value is preferable as it considers a broader range of neighbors for classification. A reasonable compromise could be setting k to 5, which balances the need for a smoother decision boundary to avoid sensitivity to outliers (as with k = 1) while still being detailed enough to capture the complexities of true class boundaries compared to a larger k value like 50, which might oversimplify and lead to underfitting. In scenarios where the decision boundary becomes ambiguous, k = 50 may fail to capture fine details of the data."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.4
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.4
    answers["(a) P(A=1|-)"] = 0.8
    answers["(a) P(B=1|-)"] = 0.0
    answers["(a) P(C=1|-)"] = 0.4

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "1. Firstly, determine how often the attribute occurs when the outcome is positive. This involves tallying the instances where the attribute equals 1 and the class is positive. Next, calculate the total number of positive occurrences. 2. Next, repeat the process for negative outcomes. Count how many times the attribute equals 1 when the class is negative. 3. Calculate the probability of the attribute being 1 given a positive outcome by dividing the count from step 1 by the total count of positive occurrences. 4. Calculate the probability of the attribute being 1 given a negative outcome using the count from step 2 and the total count of negative occurrences. In summary, this process involves examining the relationship between an attribute being 1 and the outcome being positive or negative, and then quantifying these relationships through probability calculations."

    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.064
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "In a Naive Bayes scenario where all features are set to 1, the classifier predicts the positive class. Consequently, the conditional probability of any feature given the negative class becomes zero, leading to a joint likelihood of the negative class being precisely zero. Hence, the only feasible prediction is the positive class."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.3
    answers["(c) P(A=1,B=1)"] = 0.1

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "No"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.7
    answers["(d) P(A=1,B=0)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "No"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.4
    answers["(e) P(A=1|+)"] = 0.8
    answers["(e) P(B=1|+)"] = 0.5

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "Yes"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "In essence, A and B are dependent on each other only when considering the class they belong to. This dependency arises due to the requirement for conditional independence within the Naive Bayes classifier framework. Specifically, A and B are considered conditionally independent under a given class when the probability of both A and B occurring given that class is equal to the product of the probabilities of A and B occurring individually given that same class."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
