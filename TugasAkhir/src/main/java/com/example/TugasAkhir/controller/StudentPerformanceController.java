package com.example.TugasAkhir.controller;

import com.example.TugasAkhir.request.StudentPerformanceRequest;
import org.springframework.web.bind.annotation.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/predict")
public class StudentPerformanceController {

    @PostMapping("/performance")
    public String predictPerformance(@RequestBody StudentPerformanceRequest request) {
        try {
            // Path Python interpreter dan script
            String pythonInterpreter = "C:\\VSCode\\Python\\python.exe";
            String scriptPath = "C:\\VSCode\\__Project\\__ProjectStudiIndependen_1\\archive_2\\archive_2\\Save_Load_cmd.py";

            // Parameter yang akan dikirim ke script Python
            String[] command = {
                    pythonInterpreter,
                    scriptPath,
                    "--Age", String.valueOf(request.getAge()),
                    "--Gender", String.valueOf(request.getGender()),
                    "--Ethnicity", String.valueOf(request.getEthnicity()),
                    "--ParentalEducation", String.valueOf(request.getParentalEducation()),
                    "--StudyTimeWeekly", String.valueOf(request.getStudyTimeWeekly()),
                    "--Absences", String.valueOf(request.getAbsences()),
                    "--Tutoring", String.valueOf(request.getTutoring()),
                    "--ParentalSupport", String.valueOf(request.getParentalSupport()),
                    "--Extracurricular", String.valueOf(request.getExtracurricular()),
                    "--Sports", String.valueOf(request.getSports()),
                    "--Music", String.valueOf(request.getMusic()),
                    "--Volunteering", String.valueOf(request.getVolunteering()),
                    "--GPA", String.valueOf(request.getGpa()),
                    "--GradeClass", String.valueOf(request.getGradeClass())
            };

            // Menjalankan proses Python
            ProcessBuilder processBuilder = new ProcessBuilder(command);
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();

            // Membaca output dari script Python
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder output = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            int exitCode = process.waitFor();
            if (exitCode != 0) {
                return "Error: Script exited with code " + exitCode;
            }

            return output.toString();

        } catch (Exception e) {
            e.printStackTrace();
            return "Error: " + e.getMessage();
        }
    }
}