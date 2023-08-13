const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('file-input');
const uploadedFiles = document.getElementById('uploaded-files');
const submitForm = document.getElementById('submit-form');


dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.classList.add('drag-over');
});

dropArea.addEventListener('dragleave', (e) => {
    e.preventDefault();
    dropArea.classList.remove('drag-over');
});

dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dropArea.classList.remove('drag-over');

    const files = e.dataTransfer.files;
    handleFiles(files, uploadedFiles);
});

fileInput.addEventListener('change', (e) => {
    const files = e.target.files;
    handleFiles(files, uploadedFiles);
});

function handleFiles(files, uploadedFiles) {
    uploadedFiles.innerHTML = ''; // Clear previous content

    for (const file of files) {
        const fileDiv = document.createElement('div');
        fileDiv.textContent = file.name;
        uploadedFiles.appendChild(fileDiv);
    }
}

submitForm.addEventListener('submit', (e) => {
    if (!fileInput.files.length) {
        e.preventDefault();
        alert('파일을 선택하세요.');
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
});