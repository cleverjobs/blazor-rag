# Issue saving and re-applying GridState after 4.0 upgrade

## Question

**Gre** asked on 01 Feb 2023

For over a year I've been saving GridState changes to local storage and then re-applying them when a user returns to that grid. Been working with no issues. I use FilterMode="GridFilterMode.FilterRow" in my grids. Upon upgrading to 4.0 this no longer works, the grid thinks there are filters but they are not applied correctly. I'm thinking this is due to this breaking change. It would be good to get some more details of this change and why it was made? Cant find any details for it. FilterRow uses CompositeFilterDescriptor instead of FilterDescriptor. The odd thing now is FilterDescriptors always use a logical AND and seem to include an additional filter, ie: on a string contains filter, where the field needs to include a null. Below is an example of a contains filter on an example first and last name fields. The additional clauses expecting them to contain a null are not added by me but rather automatically by the grid. [
{
"LogicalOperator": 0,
"FilterDescriptors": [
{
"Member": "FirstName",
"Operator": 8,
"Value": "d"
},
{
"Member": "FirstName",
"Operator": 8,
"Value": null
}
]
},
{
"LogicalOperator": 0,
"FilterDescriptors": [
{
"Member": "LastName",
"Operator": 8,
"Value": "b"
},
{
"Member": "LastName",
"Operator": 8,
"Value": null
}
]
}
] This state is saved as is in local storage, when a user leaves this screen and returns and the state is re-applied (again this has been working for a year prior to 4.0) the state gets re-applied like the bottom json with 2 filters to blank member names. It seems like to me theres a bug in the re-apply of filters where the grid is not expecting composite filters now?? If I can provide any further details please let me know. [
{
"Member": "",
"Operator": 2,
"Value": null
},
{
"Member": "",
"Operator": 2,
"Value": null
}
]

### Response

**Greg** commented on 01 Feb 2023

I've figured out the cause of this breaking change, Telerik uses a custom json converter for filter descriptors called 'FilterDescriptorConverter'. This looks for the existence of a property called "LogicalOperator" which is part of a composite filter but not a regular filter. And this is how it decides which type it is. The problem is the default AND logical operator is value 0, which is also the default for the enum. So if you ignore defaults when serializing the json then this property will not be written, even though this should be valid to serialize/deserialize this way! Because Telerik now relies on the "LogicalOperator" property being present this breaks. If I change my serializer to write all default values this problem is fixed. HOWEVER, this really bloats the size of the grid states being serialized and written to local storage, ie: every column has defaults for properties like "Locked" and "Visible" which now ALL must be written. So this is really unfortunate, and a symptom of some questionable? logic where the Telerik FilterDescriptorConverter relies on the existence of a specific property name to decide how to serialize each filter descriptor. TLDR; anyone that uses a filter row and saves grid state without serializing all properties with default values will now be broken as of 4.0 Would be interested to hear if theres a better solution to this problem.

### Response

**Hristian Stefanov** commented on 06 Feb 2023

Hi Greg, Great observations! I'm glad to see that you've managed to adjust your configuration based on the latest breaking changes. Indeed, regarding filtering, as of the 4.0 version, the Grid uses only CompositeFilterDescriptor for both - FilterRow and FilterMenu. One of the main benefits of that breaking change is consistency in both filtering types' structures. As a result, now a Grid with FilterRow needs to present LogicalOperator in the LocalStorage JSON, similar to Grid with FilterMenu, so the CompositeFilterDescriptor is set correctly. Regarding the other part of the provided information, I will need a little more time to review it fully. I will get back to you very shortly with more details. Thank you for your patience.

### Response

**Hristian Stefanov** commented on 16 Feb 2023

Hi Greg, The testing and reviewing of the second part of the information took a little longer than expected. I'm very sorry about that. I wanted to make sure that everything between the versions is tested. I tested several samples that save the Grid state in LocalStorage in different versions. As a result, the column properties of type Locked, Visible, etc. are always present in the JSON with their default value, even if they are not needed, no matter the version. After several attempts, I'm still unable to reproduce such problematic bloat in the size. Maybe I'm missing something from the actual project that will help me reproduce. We are always open to improvements, so if you have ideas or more feedback on the latest changes, please share them. If there is still a remaining problem with the size of the state, send us a small runnable sample that uses the actual configuration. That will allow me to debug and see the configuration problems on my machine. Let me know if we can assist with more information.

### Response

**Greg** commented on 16 Feb 2023

What are you using for doing the JSON serialization of the grid state? Are you using the dotnet System.Text.Json serializer? Try setting the "DefaultIgnoreCondition" for the serializer options to "WhenWritingDefault". I would argue this is a common practice as this will ignore writing any reference type property where the value is null or any value type with a default, ie: boolean that is false, integer that is zero, etc. This is what we do in all of our projects for efficiency. By serializing JSON this way it can in some cases drastically reduce the size needed to read/write to local storage. Because of the changes made in 4.0 this will break for anyone serializing using this option. This is because the Telerik 'FilterDescriptorConverter' relies on the existence of a property to decide if the filter is composite or not. By doing this it means the property "LogicalOperator" must be written whether it has a default value or not. In my opinion this is very fragile logic, it will now break if the property isnt there. I would suggest a better way would be writing a "FilterType" property that could be an enum 0 or 1 and then make the decision on the value rather then relying on the existence of the "LogicalOperator" property. By forcing users of the grid to write ALL properties with defaults it now means writing potentially hundreds of un-needed properties, ie: booleans like Visible and Locked where the values are false. If Telerik does leave it this way, I would suggest a big warning on the grid state help pages and examples that the entire grid state must be serialized, including all properties that have default values.

### Response

**Hristian Stefanov** commented on 21 Feb 2023

Hi Greg, Thank you for continuously sharing your thoughts on the updates. Indeed, I was testing with System.Text.Json. The main factor, in this case, is that the different developers use different settings/methods for serialization. As always, breaking changes require some changes in configurations, and it is true that sometimes this can be frustrating. However, I will for sure share your latest feedback and expectations with the team and it will be explored for feasible improvements. If an idea appears for change in the new updates, I will create an item on our Public Feedback Portal. At this stage, I confirm that no further descriptor changes are planned in Grid and the current updates stand. If we can assist with anything else, I'm at your disposal.
