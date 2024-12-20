import java.io.BufferedReader;
import java.io.InputStreamReader;

public class RunPythonScript {
    public static void main(String[] args) {
        try {
            // Command to run the Python script with arguments
            String[] command = {
                "python", 
                "Save_Load_cmd.py", 
                "--Age", "18",
                "--Gender", "1", 
                "--Ethnicity", "1",
                "--ParentalEducation", "4", 
                "--StudyTimeWeekly", "15", 
                "--Absences", "3", 
                "--Tutoring", "1", 
                "--ParentalSupport", "3", 
                "--Extracurricular", "1", 
                "--Sports", "1", 
                "--Music", "0", 
                "--Volunteering", "1", 
                "--GPA", "3.5", 
                "--GradeClass", "85.5"
            };

            // Start the process
            ProcessBuilder processBuilder = new ProcessBuilder(command);
            processBuilder.redirectErrorStream(true); // Combine standard output and error streams
            Process process = processBuilder.start();

            // Capture the output of the script
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Wait for the process to complete and get the exit status
            int exitCode = process.waitFor();
            System.out.println("Exited with code: " + exitCode);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}