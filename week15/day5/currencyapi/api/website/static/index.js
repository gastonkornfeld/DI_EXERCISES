function deleteNote(noteId) {
    fetch("/delete-note", { /// the url of the function
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }