# Activate buttons on change any of the fields in a model

## Question

**Pau** asked on 07 Sep 2022

Hi Add the top of a Edit form we have two buttons to Save (Opslaan) or Cancel (Annuleren) changes made to the form (model) We nog have a OnChange like event on each control but that result gives strange results , the typing in goes wronf (some charachters are skipped) So the question is: If i want to enabled the 2 buttons only when some field has changed, what is the best way to do this? Also when i reverse the changes the buttons shoud go back in disabled state Thanks for helping me! Eric

## Answer

**Hristian Stefanov** answered on 09 Sep 2022

Hi Eric, Thank you for explaining in such detail the situation. As far as I understand, the desired result is to disable/enable the Form buttons based on whether a field has value. In such a case, I confirm that it is easily achievable by using a bool flag for the " Enabled " parameter of the buttons that indicates when the field is empty. I have prepared an example for you - REPL link to demonstrate the above approach. You can run and test it to see the result. If the case is different, please modify the REPL example to show/reproduce the scenario. That will allow me to see the situation better and suggest a more suitable approach. Regards, Hristian Stefanov
