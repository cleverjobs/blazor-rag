# Nested table (Show and Hide)

## Question

**Pon** asked on 22 Mar 2023

I have two tables: Team Basic Info and Team Stats Considering the yellow cells. Team Basic Info and Team Stats are two Buttons. Team Basic Info is the default View. How can I implement the Team Stats Button so it shows the team stats table and hides the Team Basic Info and vice-versa? Thanks for any help

### Response

**Hristian Stefanov** commented on 27 Mar 2023

Hi Ponlu, As far as I understand, the desired result is to show/hide upon button clicking two Grid components with different data. In such a case, I have prepared an example for you in this REPL link. Please run and test the REPL to see if it covers your needs. In short, to achieve the desired result, create a bool variable that determines which Grid (table) is visible based on which button is clicked. Let me know if you find difficulties upon testing. Kind Regards, Hristian
