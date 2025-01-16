import java.io.File;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Slider;
import javafx.scene.input.MouseEvent;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;
import javafx.stage.FileChooser;

public class MediaPlayerController {

    @FXML
    private Button btnPlay;

    @FXML
    private Button btnStop;

    @FXML
    private MediaView mediaView;

    @FXML
    private Slider slider; // This is the progress bar slider

    private Media media;
    private MediaPlayer mediaPlayer;
    private boolean isPlayed = false;

    @FXML
    void btnPlay(MouseEvent event) {
        if (!isPlayed) {
            btnPlay.setText("Pause");
            mediaPlayer.play();
            isPlayed = true;
        } else {
            btnPlay.setText("Play");
            mediaPlayer.pause();
            isPlayed = false;
        }
    }

    @FXML
    void btnStop(MouseEvent event) {
        btnPlay.setText("Play");
        mediaPlayer.stop();
        isPlayed = false;
        slider.setValue(0);  // Reset the slider when stopped
    }

    @FXML
    void selectMedia(ActionEvent event) {
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Select Media");
        File selectedFile = fileChooser.showOpenDialog(null);

        if (selectedFile != null) {
            String url = selectedFile.toURI().toString();

            media = new Media(url);
            mediaPlayer = new MediaPlayer(media);
            mediaView.setMediaPlayer(mediaPlayer);

            Scene scene = mediaView.getScene();
            mediaView.fitWidthProperty().bind(scene.widthProperty());
            mediaView.fitHeightProperty().bind(scene.heightProperty());

            // Set up slider max to the media duration once the media is ready
            mediaPlayer.setOnReady(() -> {
                slider.setMax(mediaPlayer.getMedia().getDuration().toSeconds());
            });

            // Update slider as the media plays
            mediaPlayer.currentTimeProperty().addListener((observable, oldValue, newValue) -> {
                if (!slider.isValueChanging()) {  // Avoid interfering when user is dragging
                    slider.setValue(newValue.toSeconds());
                }
            });

            // Enable seeking to new position when the slider is dragged
            slider.setOnMousePressed(event1 -> mediaPlayer.pause()); // Pause while dragging

            slider.setOnMouseReleased(event1 -> { // Seek to new position on release
                mediaPlayer.seek(javafx.util.Duration.seconds(slider.getValue()));
                if (isPlayed) {
                    mediaPlayer.play(); // Resume play if it was playing
                }
            });

            mediaPlayer.play();
            btnPlay.setText("Pause");
            isPlayed = true;
        }
    }
}