/* global bootstrap */

const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Edit Functionality Initialization
/**
 * Initializes edit functionality for the provided edit buttons.
 * @param {HTMLCollectionOf<Element>} editButtons - Collection of edit buttons.
 * @param {HTMLTextAreaElement} commentText - Text area for comment input.
 * @param {HTMLFormElement} commentForm - Comment form.
 * @param {HTMLButtonElement} submitButton - Submit button.
 */
Array.from(editButtons).forEach(button => {
  button.addEventListener("click", (event) => {
    const commentId = event.target.getAttribute("data-comment_id");
    const commentContent = document.getElementById(`comment${commentId}`).innerText;

    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
});

// Deletion Functionality Initialization
/**
 * Initializes deletion functionality for the provided delete buttons.
 * @param {HTMLCollectionOf<Element>} deleteButtons - Collection of delete buttons.
 * @param {HTMLAnchorElement} deleteConfirm - Delete confirmation link.
 * @param {Modal} deleteModal - Bootstrap modal for deletion confirmation.
 */
Array.from(deleteButtons).forEach(button => {
  button.addEventListener("click", (event) => {
    const commentId = event.target.getAttribute("data-comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
});
