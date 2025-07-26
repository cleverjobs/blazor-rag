# How to BUnit test a Combobox.

## Question

**Dal** asked on 10 Jan 2022

I have a ComboBox that needs to be unit tested. It autocompletes and populates a list of addresses utilizing services. Currently this works perfect in the UI version and I am wanting to write unit tests which accomplish the following. 1. Enter Full AddressTextin to the combo box 2. List of potential addresses populates via a Mock Address Lookup Service (in this case only 1, because I am entering the full address). 3. Matching item is selected, and AddressID obtained. 4. ID is compared against expected Id. I am currently using BUnit tests, and I am unsure how to proceed with creating unit tests for this combo box that follow the above steps. How do I trigger the "Blur" or setting the value after using the .Input(addresstext) of the Element.

## Answer

**Svetoslav Dimitrov** answered on 12 Jan 2022

Hello Dale, Testing UI components with the bUnit testing framework is not truly easy to achieve. The best way to test the UI components of an application would be to create end-to-end (e2e) tests. Testing frameworks like selenium would allow you to simulate clicks, scrolling, and test every aspect of the components. Regards, Svetoslav Dimitrov
