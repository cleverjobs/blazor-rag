# Show , save/restor filter

## Question

**Pau** asked on 11 May 2022

Hi Using Filtermenu , an user set a filter on multiple columns, i want to save this filter in the database and reuse it later. Is this possible. Also when filtering , the user can not see what filters he or she placed. Can it be possible to have a grid property that describes the filter like ( A> 10) And ( (B=2) or B=3) ) and COUNTRY='USA" ? This way we can drop a label and attach t to the property Eric

## Answer

**Svetoslav Dimitrov** answered on 13 May 2022

Hello Eric, If you want to print the filter to the user, so that can see it at any time, you can use the Grid state to get the filter descriptors and use them to construct the string you would like your users to see. You can also save that string in the database in an appropriate format so that the Grid can reuse it ( see the set Grid options with the state section ). Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Paul** answered on 13 May 2022

Hi I understand , but it would be nice if Telerik makes a Grid property returning the constructed string, instead of letting every customer who wants this do its own code. Thats wht we buy components :-) Eric

### Response

**Paul** commented on 18 May 2022

Hi In the gray part above the grid the user can see a filter was mdae on field "Indienst=1" and (Department='HRM' or Department='Inkoop' ) This is importand for the user to knowm how can he remember which values where selected? Eric

### Response

**Svetoslav Dimitrov** commented on 18 May 2022

Hello Eric, I will provide your feedback to our management team to determine if such a feature would be applicable to the Grid or the Filter component. After that discussion, I will make a sample implementation to showcase how this can be done.

### Response

**Svetoslav Dimitrov** commented on 20 May 2022

Hello Eric, I have made an example of how to achieve the behavior. You can see it from this REPL link. Could you let me know if such a filter string is appropriate for your application?

### Response

**Paul** answered on 20 May 2022

Hi Svetoslav Looks a lot as I would like it to be , thanks for the effort! In this case you should add () like ( ( Id isEqualTo 5 ) OR ( Id isGreaterThan 20 ) ) AND ( Name contains “25”) Also with numeric colums no “” around the value Also offer a possibility to change the text for “isEqualTo” , “isGreatherThan” , “contains” and “OR” and “AND” to do translations (also for other comparisons We will use the dropdownchecklistbox a lot so it also should work on these. Thanks so far!!

### Response

**Svetoslav Dimitrov** commented on 25 May 2022

Hello Eric, To each question in its respective turn: Further enhancements in the Fitler string: I have added some more improvements to the way the string is formatted and you can see it from this REPL link. could you run it and let me know if it suits your application needs? Translating the FilterOperator: This is indeed possible through localization and globalization. I would encourage you to give the Localization and Globalization online demo where these strings are localized.

### Response

**Paul** commented on 25 May 2022

Hi Svetoslav (nice name) i have set 2 filters on team and on Id , in the filterstring ther should be a 'And' between them Thanks for the effort! Eric

### Response

**Paul** commented on 25 May 2022

Hi can you add a checklistbox filter in the demo? Eric

### Response

**Svetoslav Dimitrov** commented on 27 May 2022

Hello Eric, I have modified the REPL snippet to work with both FilterMenuType.Menu and FilterMenuType.CheckBoxList. You can further manipulate that string to match the exact needs of your application. As a general rule, we as support agents prove assistance when using the built-in functionality of the Grid. Custom implementations and tweaks should be implemented by the application.

### Response

**Paul** commented on 30 May 2022

Hi Now its works, great love it! Just a 'And' between the two conditions needs to be a added Eric

### Response

**Svetoslav Dimitrov** commented on 02 Jun 2022

Hello Eric, You can add the "And" word in multiple ways. One way would be in the OnStateChangedHandler to use a for loop instead of a foreach and for each iteration of the loop add an "And", but for the very last iteration. This is probably the best and easiest way to achieve the desired behavior.

### Response

**Paul** commented on 02 Jun 2022

Hi Why should we do this, its more simple if you add it. We want to display this string to the end user so he or she can see on which values selections are made? So it should be a readable string which it now is not, so please add it Eric

### Response

**Svetoslav Dimitrov** commented on 07 Jun 2022

Hello Eric, You can refer to the modified version of the REPL link.

### Response

**Paul** commented on 07 Jun 2022

Hi Looking fine now Please not create a property Filterstring on thr grid so we, as developers just have to read the property and show it to the users Thanks! Eric

### Response

**Paul** commented on 07 Jun 2022

haha I mean please now create a propety filterstring Eric

### Response

**Svetoslav Dimitrov** commented on 09 Jun 2022

Hello Eric, Such built-in functionality would be more suitable for the Filter component. I have opened a feature request for a human-readable string for the Filter component. You are automatically subscribed to receive email notifications for status updates and I have added your Vote for it.
