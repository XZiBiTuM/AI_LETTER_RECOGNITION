        window.addEventListener('DOMContentLoaded', function() {
            var savedSrc = localStorage.getItem('imageSrc');
            if (savedSrc) {
                document.getElementById('image-preview').setAttribute('src', savedSrc);
            }
        });

        document.getElementById('image-upload').addEventListener('change', function() {
            var file = this.files[0];
            if (file) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    var imagePreview = document.getElementById('image-preview');
                    imagePreview.setAttribute('src', e.target.result);
                    localStorage.setItem('imageSrc', e.target.result);
                }
                reader.readAsDataURL(file);
            } else {
                document.getElementById('image-preview').removeAttribute('src');
                localStorage.removeItem('imageSrc');
            }
        });
        document.getElementById('upload-form').addEventListener('submit', function(e) {
        e.preventDefault();
        let formData = new FormData(this);
        fetch('', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Bad Request');
            }
            return response.json();
        })
        .then(data => {
                const letterMapping = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
    5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
    15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'V', 21: 'W', 22: 'X', 23: 'Y', 24: 'Z'
    };

    const predictedLetter = letterMapping[data.prediction];

    document.getElementById('prediction_result').innerText = 'Результат: ' + predictedLetter;
        })
        .catch(error => {
            if (error.message === 'Bad Request') {
                document.getElementById('prediction_result').innerText = 'Ошибка: Неверный запрос (возможно, изображение устарело, загрузите его снова)';
            } else {
                console.error('Ошибка:', error);
            }
        });
    });

    function clearLocalStorage() {
        localStorage.clear();
        console.log('LocalStorage очищен.');
    }

    setInterval(clearLocalStorage, 30 * 60 * 1000);