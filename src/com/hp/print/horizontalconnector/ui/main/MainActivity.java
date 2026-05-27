package com.hp.print.horizontalconnector.ui.main;
 
// ... (existing imports)
import android.app.FragmentTransaction;
import android.support.v4.app.Fragment; // For compatibility with v4 fragment
import android.widget.FrameLayout;
 
public class MainActivity extends PresenterRootBaseAppCompatActivity<MainContract.View, MainContract.Presenter>
        implements View.OnClickListener, MainContract.View, PhilipContract.View {
 
    private final String TAG = this.getClass().getName();
    // ... (existing fields)
 
    // Add this field for Copilot Chat
    private FrameLayout copilotChatContainer;
 
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // ... (existing code)
 
        // Initialize Copilot Chat UI
        copilotChatContainer = findViewById(R.id.copilot_chat_container);
        if (copilotChatContainer != null) {
            showCopilotChat();
        }
    }
 
    private void showCopilotChat() {
        Fragment chatFragment = new CopilotChatFragment();
        getSupportFragmentManager()
            .beginTransaction()
            .replace(R.id.copilot_chat_container, chatFragment)
            .commitAllowingStateLoss();
    }
 
    // ... (rest of MainActivity)
}
