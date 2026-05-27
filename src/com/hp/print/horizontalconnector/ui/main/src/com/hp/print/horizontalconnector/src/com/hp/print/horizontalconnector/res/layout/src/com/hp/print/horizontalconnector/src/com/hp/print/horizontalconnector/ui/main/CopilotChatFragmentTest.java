package com.hp.print.horizontalconnector.ui.main;
 
import android.support.v4.app.FragmentActivity;
import android.support.v7.widget.RecyclerView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
 
import com.hp.print.horizontalconnector.R;
 
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.robolectric.Robolectric;
import org.robolectric.RobolectricTestRunner;
import org.robolectric.android.controller.ActivityController;
 
import static org.junit.Assert.*;
 
@RunWith(RobolectricTestRunner.class)
public class CopilotChatFragmentTest {
 
    private FragmentActivity activity;
    private CopilotChatFragment fragment;
 
    @Before
    public void setUp() {
        activity = Robolectric.buildActivity(FragmentActivity.class).create().start().resume().get();
        fragment = new CopilotChatFragment();
        activity.getSupportFragmentManager()
                .beginTransaction()
                .add(fragment, null)
                .commitNow();
    }
 
    @Test
    public void testSendMessage_addsUserMessageAndBotReply() {
        EditText input = fragment.getView().findViewById(R.id.copilot_chat_input);
        Button send = fragment.getView().findViewById(R.id.copilot_chat_send);
        RecyclerView recycler = fragment.getView().findViewById(R.id.copilot_chat_recycler_view);
        ProgressBar progress = fragment.getView().findViewById(R.id.copilot_chat_progress);
 
        input.setText(\"Hello Copilot\");
        send.performClick();
 
        // User message should be added immediately
        assertEquals(1, recycler.getAdapter().getItemCount());
 
        // Progress bar should be visible while waiting for reply
        assertEquals(ProgressBar.VISIBLE, progress.getVisibility());
 
        // Simulate delayed response
        Robolectric.getForegroundThreadScheduler().advanceBy(1000);
 
        // Bot reply should be added
        assertEquals(2, recycler.getAdapter().getItemCount());
        assertEquals(ProgressBar.GONE, progress.getVisibility());
    }
 
    @Test
    public void testSendMessage_emptyInput_noAction() {
        EditText input = fragment.getView().findViewById(R.id.copilot_chat_input);
        Button send = fragment.getView().findViewById(R.id.copilot_chat_send);
        RecyclerView recycler = fragment.getView().findViewById(R.id.copilot_chat_recycler_view);
 
        input.setText(\"\");
        send.performClick();
 
        assertEquals(0, recycler.getAdapter().getItemCount());
    }
}
