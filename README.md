# Reletor
This is a saved search parser for your saved homes on Realtor.com. Exports to CSV for easy vieiwng in a spreadsheet.

## Usage

1. Visit Realtor.com. Sign up if you haven't - you must be signed in to use the ❤️ feature.
2. Find a bunch of houses you like the most. Click the ❤️ icon for as many houses as you want.
3. Use `Inspector` in your `Web Development Tools` of your browser (NOT `view-source:`), and copy and paste the entire HTML document into a new file, like say, `realtor.html`
4. Run the script to output to the console in tab delimited format.
5. Copy and paste the results into an excel or google spreadsheet and view the output.

## Wait, how do I run the script?

```
$ ./realtor.py realtor.html
```

