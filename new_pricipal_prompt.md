
**Advanced Data Extraction and JSON Formatting Prompt**

**Input Text:** `[Your input text goes here]`

You are tasked with a meticulous data extraction activity that requires you to carefully analyze the provided text. Your objective is to identify individuals' names along with their academic qualifications, ensuring that affiliations with universities or colleges are not included. This task demands attention to detail, particularly in maintaining the original formatting and spelling of each name as presented in the input.

**Task Overview:**

1. **Data Identification:** Scrutinize the input text to locate names and their corresponding academic qualifications. It's crucial to exclude any mentions of university or college affiliations and to consider only qualifications in their abbreviated forms (e.g., MD, BS, PhD).

2. **Data Extraction and Formatting:** Utilize the placeholders `<NAME>` and `<QUALIFICATION>` to format each identified name and qualification pair. The formatting should adhere to a specified JSON structure, which is designed to handle multiple entries.

3. **Validation:** Ensure the JSON output is correctly structured, reflecting an accurate representation of the extracted data. Each entry must be unique, and qualifications should only be included in their short form.

**Detailed Instructions:**

- Begin by reading through the provided text thoroughly to identify all instances where individuals' names are followed or preceded by their academic qualifications in abbreviated form.
- For each identified pair, note the name and qualification, ensuring the original spelling and formatting of the name are preserved.
- Format the extracted information using the provided JSON template, replacing `<NAME>` with the exact name and `<QUALIFICATION>` with the corresponding qualification abbreviation.
- Ensure the JSON structure is maintained, with each name-qualification pair formatted as a separate entry within the array.

**JSON Template:**
```json
{{
  "NAME_WITH_QUALIFICATION": [
    ["<NAME>, <QUALIFICATION>"],
    ...additional entries as needed
  ]
}}
```

**Checkpoints:**

- **Accuracy:** Confirm that each name and qualification pair is correctly extracted and formatted, with no alterations to the original name formatting.
- **Uniqueness:** Verify that there are no duplicate entries within the JSON output, with each name being distinct.
- **Validation:** Use a JSON validator to ensure the final output is syntactically correct and adheres to the JSON format.

**Final Steps:**

- Review the JSON output to confirm it meets all the specified requirements.
- Make any necessary adjustments to ensure accuracy and adherence to the task guidelines.

