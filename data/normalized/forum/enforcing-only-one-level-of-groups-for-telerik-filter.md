# Enforcing only one level of groups for telerik filter

## Question

**Bil** asked on 02 Jun 2023

I only want my users to be able to add one level of groups to their filters. For example: Color=blue AND ( height> 3 OR height <1 ) OR foo=bar I don't want them to add sub-groups to groups (adding an AND group inside of the height block in the above). Is there a way to prevent that from happening in the control?

### Response

**Nadezhda Tacheva** commented on 07 Jun 2023

Hi Bill, In order to suggest a useful solution, I'd like to first confirm with you the exact desired result. I see that you have marked to be using the Filter component together with the Grid. By design, the Filter component initializes with one group of filter descriptors. As I understand, you want to prevent the users from adding another group but they should be able to add expressions. Is that correct? If so, can you please let me know if the ability to remove the "Add group" button will serve well to achieve your desired result? If not, please share some more details about the exact behavior you are looking for, so we can evaluate it. Thank you in advance! I look forward to hearing from you.

### Response

**Bill** commented on 07 Jun 2023

I would like them to be able to add one or more groups from the top level (so they could have OR as well as AND groups). But within a sub-group, I'd like the ability to add a group below that one to be removed. So only one level of nesting groups, does that make sense?

### Response

**Nadezhda Tacheva** commented on 09 Jun 2023

Hi Bill, Thank you for the additional details! Currently, such a result can only be achieved with CSS. You can target and hide the "Add Group" button in the desired level to prevent the user from creating another nested group. Here is an example: [https://blazorrepl.telerik.com/wxEAOXlo50v2ge6k53.](https://blazorrepl.telerik.com/wxEAOXlo50v2ge6k53.) In addition, I've opened a feature request to allow one easily manage the content of the filter group toolbar. This will let you remove the "Add Group" button as needed. You can track the progress of the item here: Filter Group Toolbar Template. I added your vote there to bump its popularity as we prioritize the enhancements based on the demand. As a creator, you are automatically subscribed to get status updates.

### Response

**Bill** commented on 12 Jun 2023

Thanks so much!
