import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
import os
import evernote.edam.notestore.ttypes as NoteStore
from evernote.api.client import EvernoteClient

auth_token = ""

if auth_token == "your developer token":
    print("Please fill in your developer token")
    print("To get a developer token, visit " \
          "https://sandbox.evernote.com/api/DeveloperToken.action")
    exit(1)

sandbox=True
china=False

client = EvernoteClient(token=auth_token, sandbox=sandbox,china=china)

user_store = client.get_user_store()
note_store = client.get_note_store()

notebooks = note_store.listNotebooks()
for notebook in notebooks:
    #print(notebook.name)
    pass

note_filter = NoteStore.NoteFilter()
note_filter.words = ''
notes_metadata_result_spec = NoteStore.NotesMetadataResultSpec()
notes_metadata_result_spec.includeAttributes=True

count = note_store.findNoteCounts(note_filter,False)

num = 0

for value in count.notebookCounts.values():
    num += value

MAX = 250
offset = 0

while offset < num:
    print(offset)
    notes_metadata_list = note_store.findNotesMetadata(note_filter, offset, MAX, notes_metadata_result_spec)
    for metadata in notes_metadata_list.notes:
        if metadata.attributes.shareDate:
            note_store.stopSharingNote(metadata.guid)
    offset += MAX



