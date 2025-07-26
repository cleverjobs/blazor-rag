# Formatting within a grid column

## Question

**aeh** asked on 08 Mar 2022

Okay, this one is getting me frustrated. One of the columns that I am retrieving from the database is formatted with HTML and looks like: 17 04 01<br />17 04 02<br />17 04 05<br />20 01 40 Now, when I use webForms, the items will display like this: 17 04 01 17 04 02 17 04 05 20 01 40 However, in blazor they display like: 17 04 01<br />17 04 02<br />17 04 05<br />20 01 40 How can I get them to display like they did in webforms? I've even tried to split the string and then loop thru the results and I still cannot get them to display on separate lines.

### Response

**Roland** commented on 08 Mar 2022

use <div> @( ( MarkupString ) content ) </div>

### Response

**aehlert** commented on 08 Mar 2022

That did it! Thank you!
