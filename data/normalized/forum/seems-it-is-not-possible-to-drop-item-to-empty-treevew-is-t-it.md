# seems it is not possible to drop item to empty treevew, is`t it?

## Question

**Ale** asked on 24 Jun 2021

basically was reproduced using demos, hope it is not true :-)

## Answer

**Marin Bratanov** answered on 27 Jun 2021

Hello Aleksandr, Your observation is correct - when there is no data in the treeview, you can't drop items into it simply because it does not render anything and so there is no drop target. A solution is to ensure you always have at least one dummy node with text like "(empty)" or "(drag here)" so there is a drop target. When processing the data, you can check if this is the only item and if so - remove it so that newly added data will have its proper structure. I also added this information into a new Knowledge Base article (Pull Request here where you can preview it) so that it becomes available to other people looking for a solution for this. Regards, Marin Bratanov Progress Telerik
