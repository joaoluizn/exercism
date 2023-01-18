using System;

static class LogLine
{
    public static string Message(string logLine)
    {
        return LogLine.SplitMessage(logLine)[3].Trim();
    }

    public static string LogLevel(string logLine)
    {
        return LogLine.SplitMessage(logLine)[1].Trim().ToLower();
    }

    public static string Reformat(string logLine)
    {
        return $"{LogLine.Message(logLine)} ({LogLine.LogLevel(logLine)})";
    }

    private static string[] SplitMessage(string logline) 
    {
        char[] delimiters = {'[', ']', ':'};
        return logline.Split(delimiters);
    }
}
