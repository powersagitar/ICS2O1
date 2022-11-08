# nestedLoop.py
Table of Content
- [nestedLoop.py](#nestedlooppy)
  - [Data Structure](#data-structure)
    - [Variables](#variables)
    - [Stack Chart](#stack-chart)
  - [Pending](#pending)

## Data Structure
### Variables
* `discount`
  * Type: bool
  * Value: `True`
  * Declaration Condition: `MM` = `DD`
* `specificationStore`
  * `void`: no specifications
  * non-void: specifications

### Stack Chart
| Index |     Tag     |        Menu         | Price |
| :---: | :---------: | :-----------------: | :---: |
|   0   | meat-burger |     beefBurger      |  10   |
|   1   |   burger    |    cheeseBurger     |  10   |
|   2   | meat-burger |    doubleBurger     |  10   |
|   3   | meat-burger |    chickenBurger    |  10   |
|   4   | meat-burger |    sausageBurger    |  10   |
|   5   |  beverage   | fruitopiaStrawberry |  10   |
|   6   |  beverage   |   fruitopiaOrange   |  10   |
|   7   |  beverage   |        coke         |  10   |
|   8   |  beverage   |      dietCoke       |  10   |
|   9   |   others    |        fries        |  10   |
|  10   |   others    |      iceCream       |  10   |

## Pending
* Complete arg for each product
* Complete multi-purchase for a single product
* refunding