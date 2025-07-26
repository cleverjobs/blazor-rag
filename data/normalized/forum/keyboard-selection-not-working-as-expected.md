# Keyboard selection not working as expected

## Question

**Jef** asked on 20 Nov 2020

Keyboard selection only seems to match the first letter of the text. Is there a setting to change this behavior? I've confirmed this behavior on the Blazor UI DropDownList demo as well. If you type in the state dropdown it just keeps changing the selection to the first state that begins with the last letter typed. Without the ability to use the keyboard it makes large dropdownlists unmanageable.

## Answer

**Marin Bratanov** answered on 22 Nov 2020

Hello Jeffrey, The dropdownlist does not have other filtering/searching capabilities and this behavior is expected. You can Follow the implementation of a more advanced search/filter here: [https://feedback.telerik.com/blazor/1427877-filter-search-look-ahead.](https://feedback.telerik.com/blazor/1427877-filter-search-look-ahead.) I've added your Vote on your behalf to raise its priority. In the meantime, you can consider the combo box or autocomplete components that have that already. The ability to load data on demand through the OnRead event can also help with large data sets, because generally having thousands of items in the dropdown will slow down the page otherwise. Regards, Marin Bratanov

### Response

**Jeffrey** answered on 23 Nov 2020

Thanks Marin. I realize the Blazor components are relatively new but I hope this feature is added sooner rather than later. Even a simple dropdown of US state names can be tedious. Typing "M" 8 times to select Montana is a little much. I would argue this is a fundamental feature of a dropdownlist.

### Response

**Marin Bratanov** answered on 23 Nov 2020

Hello Jeffrey, You can use the ComboBox for that in the meantime, it will even require fewer user actions, just focusing it will let you type to get the suggestions filtered down. You can see this in action here: [https://demos.telerik.com/blazor-ui/combobox/filtering.](https://demos.telerik.com/blazor-ui/combobox/filtering.) On the implementation of similar functionality in the DropDownList - I've added your Vote on your behalf (you can do so yourself on any item you want to see implemented by clicking the Vote button on its portal page), and that raises the priority of a request. We do monitor the

### Response

**Marin Bratanov** answered on 03 Dec 2020

Hi again Jeffrey, We've been discussing this and we've logged the following enhancement idea for the component to start acting like you describe: [https://feedback.telerik.com/blazor/1497778-typing-to-select-item-should-use-all-symbols-not-only-the-first.](https://feedback.telerik.com/blazor/1497778-typing-to-select-item-should-use-all-symbols-not-only-the-first.) If you have anything to add on top of how I rephrased your query, feel free to comment. I've also added your Vote to it to raise its priority and you can click the Vote button to get status updates via email. Regards, Marin Bratanov
