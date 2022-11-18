# Menu - Nested Loop
Table of Contents
- [Menu - Nested Loop](#menu---nested-loop)
  - [Pricing](#pricing)
  - [Variable use](#variable-use)
  - [Thinking](#thinking)
  - [Efficiency analysis](#efficiency-analysis)
  - [How to add new features](#how-to-add-new-features)
    - [adding new items to the menu](#adding-new-items-to-the-menu)
    - [adding new specifications](#adding-new-specifications)

## Pricing (Menu)
| Index |         Menu         |     Tag     | Price |
| :---: | :------------------: | :---------: | :---: |
|   1   |     beef burger      | meat-burger |  15   |
|   2   |    cheese burger     |   burger    |  14   |
|   3   |    double burger     | meat-burger |  25   |
|   4   |    chicken burger    | meat-burger |  13   |
|   5   |    sausage burger    | meat-burger |  15   |
|   6   |   fruitopia orange   |  beverage   |   5   |
|   7   | fruitopia strawberry |  beverage   |   5   |
|   8   |         coke         |  beverage   |   5   |
|   9   |      diet coke       |  beverage   |   5   |
|  10   |        fries         |   others    |  15   |
|  11   |      ice cream       |   others    |   5   |

## Variable use
|       Name       |      Data type      |                                                    Description                                                     |
| :--------------: | :-----------------: | :----------------------------------------------------------------------------------------------------------------: |
|      dateM       |         int         |                                                storing date (month)                                                |
|      dateD       |         int         |                                                 storing date (day)                                                 |
|       menu       |       string        |                                                    storing menu                                                    |
|       tag        |       string        |                                         storing tags for items in the menu                                         |
|      PRICE       |    const string     |                                               storing original price                                               |
|       cart       |       string        |                                               storing ordered items                                                |
|   refundToken    |        bool         |                                         storing refund request eligibility                                         |
|  customerCount   |         int         |                                      storing customer count for data analysis                                      |
|     revenue      |        float        |                                         storing revenue for data analysis                                          |
| donationReceived |        float        |                                 storing total received donation for data analysis                                  |
|     DISCOUNT     |     const bool      |                                            storing discount eligibility                                            |
|    userInput     | ambiguous (varying) |                                            storing temporary user input                                            |
|   actualPrice    |       string        |                                                storing actual price                                                |
|     subtotal     |        float        |                                              storing actual subtotal                                               |
|       tax        |        float        |                                                    storing tax                                                     |
| originalSubtotal |        float        |                                             storing original subtotal                                              |
|       name       |       string        |                                               storing customer name                                                |
|  specification   |       string        |                                          storing customer specifications                                           |
|      start       |         int         | storing temporary info for the substring starting range in a string (a key variable why can use strings as arrays) |
|       end        |         int         |  storing temporary info for the substring ending range in a string (a key variable why can use strings as arrays)  |
|      parts       |       string        |   storing temporary info for the substring finding index function (a key variable why can use strings as arrays)   |
|      index       |         int         | storint temporary info for the substring's nth occurrences' indexes (a key variable why can use strings as arrays) |
|        i         |         int         |                               interation variable, storing temporary interation info                               |
|       argu       |       string        |                                            storing temporary item sizes                                            |
|      refund      |         int         |                                   storing temporary info for the refunding queue                                   |
|     donation     |        float        |                                        storing temporary info for donations                                        |

## Thinking
* use strings as arrays
  * divider choice: '|'
    * reason: have no conflict with possible user input and Python syntax
  * the indicator is the first '|' inside a pair of two '|'s
* use donation instead of tipping due to it's a fast-food restaurant
  
## Efficiency analysis
* if functions are allowed to use, the code can be shrunk significantly (simplify use of repetitive code blocks)
  * the algorithm to find out the index of the nth occurrence of a specific substring
  * updating actual price (avoiding specifications and applying discounts)
  * printing menu 
  * size choosing (same code block appears both in mode purchase and mode refund)
  * price calculation (including both regular calculation and with discount(the additional original price))
* why souce file has 334 lines
  * it used to be neat (150 lines) when i just finished the menu printing and other basic features, becomes less efficient when adding support for exceptions and sub-menu selector (have no idea how to optimize temporarily)

## How to add new features
### adding new items to the menu
  * modify `menu`, `tag`, and `PRICE` variables in line 28-30, no other modifications are needed (unless a new tag is created)
### adding new specifications
  * update currently available specification list in line 65
  * duplicate the specification template (line 69-84), change the `veggie` to the new custom keyword, and change the `meat` to the new filter