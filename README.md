# Translation File Organization

For each item in the Services section of The Pavement website and for each language a separate file containing the text translation is created.

The organization of a translation file for a particular item and a particular language is as follows:

* **File name** - the same as the title of the item with all letter small caps, all spaces replaced by `-` and a file extension of `.md`. All other characters remain the same. Any characters which are not supported get removed. For example:

    ```
    Item name: ACTION FOR CHILDREN (GEN R 8 PROJECT)
    File name: action-for-children-(gen-r-8-project).md
    ```

* **Text organization** - the translation file consists of the following sections (in this order). Look at existing translations for examples.
    * *Original text* - each section in the item is separated from the next one by a blank line (for readability)
    * *Separator* - separates the original text from the translation: a blank line, followed by `--`, followed by another blank line
    * *Translation* - each section in the translation is separated from the next one by a blank line (for readability). Same as the original text section.

* **File location** - the file is located in a directory named after the specific subsection of the Services section of the website, which in turn is located in the `services` directory, which in turn is located in the directory corresponding to the translation language.

# Common Directory

Every language directory contains a common directory which contains translations of common expressions which might occur in multiple items.
